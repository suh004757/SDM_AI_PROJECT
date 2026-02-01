"""
LLM Router - Intelligent LLM Selection and Routing
Routes requests to appropriate LLM based on cost, capability, and availability
"""

from typing import Optional, List, Dict, Any
from enum import Enum
import logging

from ..llm_client import BaseLLMClient, LLMResponse, Message
from ..Clients import ClaudeClient, OpenAIClient, GeminiClient, LocalLLMClient
from ..config import get_config

logger = logging.getLogger(__name__)


class TaskComplexity(Enum):
    """Task complexity levels for routing decisions"""
    SIMPLE = "simple"  # Simple tasks, can use local LLM
    MODERATE = "moderate"  # Moderate tasks, use cheaper cloud models
    COMPLEX = "complex"  # Complex reasoning, use best models


class LLMRouter:
    """
    Intelligent router for selecting appropriate LLM
    Supports cost-based, capability-based, and fallback routing
    """
    
    def __init__(self):
        """Initialize router with available clients"""
        self.config = get_config()
        self.clients: Dict[str, BaseLLMClient] = {}
        self._initialize_clients()
    
    def _initialize_clients(self) -> None:
        """Initialize all available LLM clients"""
        # Try to initialize each client
        try:
            if self.config.is_configured('claude'):
                self.clients['claude'] = ClaudeClient()
                logger.info("Claude client initialized")
        except Exception as e:
            logger.warning(f"Could not initialize Claude client: {e}")
        
        try:
            if self.config.is_configured('openai'):
                self.clients['openai'] = OpenAIClient()
                logger.info("OpenAI client initialized")
        except Exception as e:
            logger.warning(f"Could not initialize OpenAI client: {e}")
        
        try:
            if self.config.is_configured('gemini'):
                self.clients['gemini'] = GeminiClient()
                logger.info("Gemini client initialized")
        except Exception as e:
            logger.warning(f"Could not initialize Gemini client: {e}")
        
        try:
            self.clients['local'] = LocalLLMClient()
            logger.info("Local LLM client initialized")
        except Exception as e:
            logger.warning(f"Could not initialize Local LLM client: {e}")
    
    def get_client(self, provider: str) -> Optional[BaseLLMClient]:
        """
        Get specific client by provider name
        
        Args:
            provider: Provider name ('claude', 'openai', 'gemini', 'local')
            
        Returns:
            LLM client or None if not available
        """
        return self.clients.get(provider.lower())
    
    def select_by_cost(
        self,
        complexity: TaskComplexity = TaskComplexity.MODERATE,
        prefer_local: bool = True
    ) -> BaseLLMClient:
        """
        Select LLM based on cost optimization
        
        Args:
            complexity: Task complexity level
            prefer_local: Prefer local LLM when possible
            
        Returns:
            Selected LLM client
        """
        # For simple tasks, prefer local LLM (free)
        if complexity == TaskComplexity.SIMPLE and prefer_local:
            if 'local' in self.clients:
                logger.info("Selected local LLM (cost: $0)")
                return self.clients['local']
        
        # For moderate tasks, use cheaper cloud models
        if complexity == TaskComplexity.MODERATE:
            # Gemini Pro is cheapest cloud option
            if 'gemini' in self.clients:
                logger.info("Selected Gemini (cost-effective)")
                return self.clients['gemini']
            # Fallback to GPT-3.5 or Claude Haiku
            if 'openai' in self.clients:
                logger.info("Selected OpenAI (moderate cost)")
                return self.clients['openai']
        
        # For complex tasks, use best models
        if complexity == TaskComplexity.COMPLEX:
            # Claude Sonnet 3.5 is best for complex reasoning
            if 'claude' in self.clients:
                logger.info("Selected Claude (best capability)")
                return self.clients['claude']
            # Fallback to GPT-4
            if 'openai' in self.clients:
                logger.info("Selected OpenAI GPT-4 (high capability)")
                return self.clients['openai']
        
        # Ultimate fallback: any available client
        if self.clients:
            fallback = next(iter(self.clients.values()))
            logger.warning(f"Using fallback client: {fallback.__class__.__name__}")
            return fallback
        
        raise RuntimeError("No LLM clients available")
    
    def select_by_capability(self, required_features: List[str]) -> BaseLLMClient:
        """
        Select LLM based on required capabilities
        
        Args:
            required_features: List of required features
                - 'long_context': Supports long context windows
                - 'function_calling': Supports function calling
                - 'vision': Supports image inputs
                - 'fast': Optimized for speed
                
        Returns:
            Selected LLM client
        """
        # Feature matrix
        capabilities = {
            'claude': ['long_context', 'function_calling', 'vision'],
            'openai': ['long_context', 'function_calling', 'vision'],
            'gemini': ['long_context', 'vision'],
            'local': ['fast'],
        }
        
        # Find best match
        best_match = None
        best_score = -1
        
        for provider, features in capabilities.items():
            if provider not in self.clients:
                continue
            
            # Calculate match score
            score = sum(1 for f in required_features if f in features)
            
            if score > best_score:
                best_score = score
                best_match = provider
        
        if best_match:
            logger.info(f"Selected {best_match} based on capabilities")
            return self.clients[best_match]
        
        # Fallback
        return self.select_by_cost(TaskComplexity.MODERATE)
    
    def generate_with_fallback(
        self,
        prompt: str,
        preferred_providers: Optional[List[str]] = None,
        **kwargs
    ) -> LLMResponse:
        """
        Generate text with automatic fallback on failure
        
        Args:
            prompt: Input prompt
            preferred_providers: Ordered list of providers to try
            **kwargs: Generation parameters
            
        Returns:
            LLMResponse from first successful provider
        """
        if preferred_providers is None:
            # Default fallback chain: Claude -> OpenAI -> Gemini -> Local
            preferred_providers = ['claude', 'openai', 'gemini', 'local']
        
        last_error = None
        
        for provider in preferred_providers:
            client = self.get_client(provider)
            if not client:
                logger.debug(f"Provider {provider} not available, skipping")
                continue
            
            try:
                logger.info(f"Attempting generation with {provider}")
                response = client.generate(prompt, **kwargs)
                logger.info(f"Successfully generated with {provider}")
                return response
                
            except Exception as e:
                logger.warning(f"Failed with {provider}: {e}")
                last_error = e
                continue
        
        # All providers failed
        raise RuntimeError(f"All providers failed. Last error: {last_error}")
    
    def chat_with_fallback(
        self,
        messages: List[Message],
        preferred_providers: Optional[List[str]] = None,
        **kwargs
    ) -> LLMResponse:
        """
        Chat with automatic fallback on failure
        
        Args:
            messages: Conversation messages
            preferred_providers: Ordered list of providers to try
            **kwargs: Chat parameters
            
        Returns:
            LLMResponse from first successful provider
        """
        if preferred_providers is None:
            preferred_providers = ['claude', 'openai', 'gemini', 'local']
        
        last_error = None
        
        for provider in preferred_providers:
            client = self.get_client(provider)
            if not client:
                continue
            
            try:
                logger.info(f"Attempting chat with {provider}")
                response = client.chat(messages, **kwargs)
                logger.info(f"Successfully chatted with {provider}")
                return response
                
            except Exception as e:
                logger.warning(f"Failed with {provider}: {e}")
                last_error = e
                continue
        
        raise RuntimeError(f"All providers failed. Last error: {last_error}")
    
    def get_available_providers(self) -> List[str]:
        """
        Get list of available providers
        
        Returns:
            List of provider names
        """
        return list(self.clients.keys())
    
    def get_total_stats(self) -> Dict[str, Any]:
        """
        Get combined statistics from all clients
        
        Returns:
            Dict with total tokens and costs across all providers
        """
        total_tokens = 0
        total_cost = 0.0
        provider_stats = {}
        
        for provider, client in self.clients.items():
            stats = client.get_stats()
            total_tokens += stats['total_tokens']
            total_cost += stats['total_cost_usd']
            provider_stats[provider] = stats
        
        return {
            'total_tokens': total_tokens,
            'total_cost_usd': total_cost,
            'providers': provider_stats
        }
