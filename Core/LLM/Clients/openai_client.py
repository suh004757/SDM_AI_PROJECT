"""
OpenAI API Client Implementation
Integrates with OpenAI's GPT models
"""

from typing import Optional, List, Generator, Dict, Any
import logging

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    logging.warning("openai package not installed. Install with: pip install openai")

from ..llm_client import BaseLLMClient, LLMResponse, Message
from ..config import get_config

logger = logging.getLogger(__name__)


class OpenAIClient(BaseLLMClient):
    """OpenAI API client implementation"""
    
    # Pricing as of 2026 (USD per 1M tokens)
    PRICING = {
        'gpt-4-turbo-preview': {'input_per_1m': 10.0, 'output_per_1m': 30.0},
        'gpt-4-turbo': {'input_per_1m': 10.0, 'output_per_1m': 30.0},
        'gpt-4': {'input_per_1m': 30.0, 'output_per_1m': 60.0},
        'gpt-4-32k': {'input_per_1m': 60.0, 'output_per_1m': 120.0},
        'gpt-3.5-turbo': {'input_per_1m': 0.5, 'output_per_1m': 1.5},
        'gpt-3.5-turbo-16k': {'input_per_1m': 3.0, 'output_per_1m': 4.0},
    }
    
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        """
        Initialize OpenAI client
        
        Args:
            api_key: OpenAI API key (if None, loads from config)
            model: Model identifier (if None, uses default from config)
        """
        if not OPENAI_AVAILABLE:
            raise ImportError("openai package required. Install with: pip install openai")
        
        config = get_config()
        
        # Use provided API key or load from config
        if api_key is None:
            api_key = config.openai_api_key
        
        # Use provided model or load from config
        if model is None:
            model = config.openai_default_model
        
        super().__init__(api_key=api_key, model=model)
        
        # Initialize OpenAI client
        if self.api_key:
            self.client = OpenAI(api_key=self.api_key)
        else:
            self.client = None
            logger.warning("OpenAI client initialized without API key - will fail on actual calls")
    
    def get_default_model(self) -> str:
        """Return default OpenAI model"""
        return 'gpt-4-turbo-preview'
    
    def _validate_config(self) -> None:
        """Validate API key"""
        if not self.api_key:
            logger.warning("No API key provided for OpenAI client")
    
    def generate(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: float = 0.7,
        **kwargs
    ) -> LLMResponse:
        """
        Generate text from prompt using GPT
        
        Args:
            prompt: Input prompt
            max_tokens: Maximum tokens to generate (default: 2048)
            temperature: Sampling temperature
            **kwargs: Additional OpenAI-specific parameters
            
        Returns:
            LLMResponse with generated text
        """
        if not self.client:
            raise ValueError("OpenAI client not initialized with API key")
        
        if max_tokens is None:
            max_tokens = 2048
        
        try:
            # Call OpenAI API
            response = self.client.chat.completions.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                **kwargs
            )
            
            # Extract response
            content = response.choices[0].message.content
            input_tokens = response.usage.prompt_tokens
            output_tokens = response.usage.completion_tokens
            total_tokens = response.usage.total_tokens
            
            # Calculate cost
            cost = self.calculate_cost(input_tokens, output_tokens)
            
            # Update stats
            self.total_tokens += total_tokens
            self.total_cost += cost
            
            return LLMResponse(
                content=content,
                model=self.model,
                provider='openai',
                tokens_used=total_tokens,
                cost_usd=cost,
                finish_reason=response.choices[0].finish_reason,
                metadata={
                    'input_tokens': input_tokens,
                    'output_tokens': output_tokens,
                    'finish_reason': response.choices[0].finish_reason,
                }
            )
            
        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            raise
    
    def chat(
        self,
        messages: List[Message],
        max_tokens: Optional[int] = None,
        temperature: float = 0.7,
        **kwargs
    ) -> LLMResponse:
        """
        Multi-turn conversation with GPT
        
        Args:
            messages: List of Message objects
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            **kwargs: Additional parameters
            
        Returns:
            LLMResponse with assistant's reply
        """
        if not self.client:
            raise ValueError("OpenAI client not initialized with API key")
        
        if max_tokens is None:
            max_tokens = 2048
        
        # Convert Message objects to OpenAI format
        openai_messages = [
            {'role': msg.role, 'content': msg.content}
            for msg in messages
        ]
        
        try:
            # Call OpenAI API
            response = self.client.chat.completions.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=openai_messages,
                **kwargs
            )
            
            # Extract response
            content = response.choices[0].message.content
            input_tokens = response.usage.prompt_tokens
            output_tokens = response.usage.completion_tokens
            total_tokens = response.usage.total_tokens
            
            # Calculate cost
            cost = self.calculate_cost(input_tokens, output_tokens)
            
            # Update stats
            self.total_tokens += total_tokens
            self.total_cost += cost
            
            return LLMResponse(
                content=content,
                model=self.model,
                provider='openai',
                tokens_used=total_tokens,
                cost_usd=cost,
                finish_reason=response.choices[0].finish_reason,
                metadata={
                    'input_tokens': input_tokens,
                    'output_tokens': output_tokens,
                    'finish_reason': response.choices[0].finish_reason,
                }
            )
            
        except Exception as e:
            logger.error(f"OpenAI chat error: {e}")
            raise
    
    def stream(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: float = 0.7,
        **kwargs
    ) -> Generator[str, None, None]:
        """
        Stream text generation from GPT
        
        Args:
            prompt: Input prompt
            max_tokens: Maximum tokens
            temperature: Sampling temperature
            **kwargs: Additional parameters
            
        Yields:
            Text chunks as they arrive
        """
        if not self.client:
            raise ValueError("OpenAI client not initialized with API key")
        
        if max_tokens is None:
            max_tokens = 2048
        
        try:
            stream = self.client.chat.completions.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[{"role": "user", "content": prompt}],
                stream=True,
                **kwargs
            )
            
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    yield chunk.choices[0].delta.content
                    
        except Exception as e:
            logger.error(f"OpenAI streaming error: {e}")
            raise
    
    def get_pricing(self) -> Dict[str, float]:
        """Get pricing for current model"""
        return self.PRICING.get(
            self.model,
            {'input_per_1m': 10.0, 'output_per_1m': 30.0}  # Default to GPT-4 Turbo pricing
        )
