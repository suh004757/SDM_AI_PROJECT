"""
Claude API Client Implementation
Integrates with Anthropic's Claude API
"""

from typing import Optional, List, Generator, Dict, Any
import logging

try:
    from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT
    ANTHROPIC_AVAILABLE = True
except ImportError:
    ANTHROPIC_AVAILABLE = False
    logging.warning("anthropic package not installed. Install with: pip install anthropic")

from ..llm_client import BaseLLMClient, LLMResponse, Message
from ..config import get_config

logger = logging.getLogger(__name__)


class ClaudeClient(BaseLLMClient):
    """Claude API client implementation"""
    
    # Pricing as of 2026 (USD per 1M tokens)
    PRICING = {
        'claude-3-5-sonnet-20241022': {'input_per_1m': 3.0, 'output_per_1m': 15.0},
        'claude-3-opus-20240229': {'input_per_1m': 15.0, 'output_per_1m': 75.0},
        'claude-3-sonnet-20240229': {'input_per_1m': 3.0, 'output_per_1m': 15.0},
        'claude-3-haiku-20240307': {'input_per_1m': 0.25, 'output_per_1m': 1.25},
    }
    
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        """
        Initialize Claude client
        
        Args:
            api_key: Anthropic API key (if None, loads from config)
            model: Model identifier (if None, uses default from config)
        """
        if not ANTHROPIC_AVAILABLE:
            raise ImportError("anthropic package required. Install with: pip install anthropic")
        
        config = get_config()
        
        # Use provided API key or load from config
        if api_key is None:
            api_key = config.anthropic_api_key
        
        # Use provided model or load from config
        if model is None:
            model = config.claude_default_model
        
        super().__init__(api_key=api_key, model=model)
        
        # Initialize Anthropic client
        if self.api_key:
            self.client = Anthropic(api_key=self.api_key)
        else:
            self.client = None
            logger.warning("Claude client initialized without API key - will fail on actual calls")
    
    def get_default_model(self) -> str:
        """Return default Claude model"""
        return 'claude-3-5-sonnet-20241022'
    
    def _validate_config(self) -> None:
        """Validate API key"""
        if not self.api_key:
            logger.warning("No API key provided for Claude client")
    
    def generate(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: float = 0.7,
        **kwargs
    ) -> LLMResponse:
        """
        Generate text from prompt using Claude
        
        Args:
            prompt: Input prompt
            max_tokens: Maximum tokens to generate (default: 2048)
            temperature: Sampling temperature
            **kwargs: Additional Claude-specific parameters
            
        Returns:
            LLMResponse with generated text
        """
        if not self.client:
            raise ValueError("Claude client not initialized with API key")
        
        if max_tokens is None:
            max_tokens = 2048
        
        try:
            # Call Claude API
            response = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                **kwargs
            )
            
            # Extract response
            content = response.content[0].text
            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens
            total_tokens = input_tokens + output_tokens
            
            # Calculate cost
            cost = self.calculate_cost(input_tokens, output_tokens)
            
            # Update stats
            self.total_tokens += total_tokens
            self.total_cost += cost
            
            return LLMResponse(
                content=content,
                model=self.model,
                provider='claude',
                tokens_used=total_tokens,
                cost_usd=cost,
                finish_reason=response.stop_reason,
                metadata={
                    'input_tokens': input_tokens,
                    'output_tokens': output_tokens,
                    'stop_reason': response.stop_reason,
                }
            )
            
        except Exception as e:
            logger.error(f"Claude API error: {e}")
            raise
    
    def chat(
        self,
        messages: List[Message],
        max_tokens: Optional[int] = None,
        temperature: float = 0.7,
        **kwargs
    ) -> LLMResponse:
        """
        Multi-turn conversation with Claude
        
        Args:
            messages: List of Message objects
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            **kwargs: Additional parameters
            
        Returns:
            LLMResponse with assistant's reply
        """
        if not self.client:
            raise ValueError("Claude client not initialized with API key")
        
        if max_tokens is None:
            max_tokens = 2048
        
        # Convert Message objects to Claude format
        claude_messages = []
        system_prompt = None
        
        for msg in messages:
            if msg.role == 'system':
                system_prompt = msg.content
            else:
                claude_messages.append({
                    'role': msg.role,
                    'content': msg.content
                })
        
        try:
            # Call Claude API
            api_kwargs = {
                'model': self.model,
                'max_tokens': max_tokens,
                'temperature': temperature,
                'messages': claude_messages,
                **kwargs
            }
            
            if system_prompt:
                api_kwargs['system'] = system_prompt
            
            response = self.client.messages.create(**api_kwargs)
            
            # Extract response
            content = response.content[0].text
            input_tokens = response.usage.input_tokens
            output_tokens = response.usage.output_tokens
            total_tokens = input_tokens + output_tokens
            
            # Calculate cost
            cost = self.calculate_cost(input_tokens, output_tokens)
            
            # Update stats
            self.total_tokens += total_tokens
            self.total_cost += cost
            
            return LLMResponse(
                content=content,
                model=self.model,
                provider='claude',
                tokens_used=total_tokens,
                cost_usd=cost,
                finish_reason=response.stop_reason,
                metadata={
                    'input_tokens': input_tokens,
                    'output_tokens': output_tokens,
                    'stop_reason': response.stop_reason,
                }
            )
            
        except Exception as e:
            logger.error(f"Claude chat error: {e}")
            raise
    
    def stream(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: float = 0.7,
        **kwargs
    ) -> Generator[str, None, None]:
        """
        Stream text generation from Claude
        
        Args:
            prompt: Input prompt
            max_tokens: Maximum tokens
            temperature: Sampling temperature
            **kwargs: Additional parameters
            
        Yields:
            Text chunks as they arrive
        """
        if not self.client:
            raise ValueError("Claude client not initialized with API key")
        
        if max_tokens is None:
            max_tokens = 2048
        
        try:
            with self.client.messages.stream(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}],
                **kwargs
            ) as stream:
                for text in stream.text_stream:
                    yield text
                    
        except Exception as e:
            logger.error(f"Claude streaming error: {e}")
            raise
    
    def get_pricing(self) -> Dict[str, float]:
        """Get pricing for current model"""
        return self.PRICING.get(
            self.model,
            {'input_per_1m': 3.0, 'output_per_1m': 15.0}  # Default to Sonnet pricing
        )
