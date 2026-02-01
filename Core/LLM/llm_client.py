"""
Unified LLM Client Interface
Base abstract class for all LLM integrations (Claude, OpenAI, Gemini, Local LLM)
"""

from abc import ABC, abstractmethod
from typing import Optional, Dict, Any, List, Generator
from dataclasses import dataclass
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


@dataclass
class LLMResponse:
    """Standardized response format from any LLM"""
    content: str
    model: str
    provider: str
    tokens_used: Optional[int] = None
    cost_usd: Optional[float] = None
    finish_reason: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    timestamp: datetime = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()


@dataclass
class Message:
    """Standard message format for chat conversations"""
    role: str  # 'system', 'user', 'assistant'
    content: str
    metadata: Optional[Dict[str, Any]] = None


class BaseLLMClient(ABC):
    """
    Abstract base class for all LLM clients
    Ensures consistent interface across Claude, OpenAI, Gemini, and Local LLM
    """
    
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        """
        Initialize LLM client
        
        Args:
            api_key: API key for the service (None for local LLM)
            model: Model identifier (e.g., 'claude-3-5-sonnet-20241022')
        """
        self.api_key = api_key
        self.model = model or self.get_default_model()
        self.total_tokens = 0
        self.total_cost = 0.0
        self._validate_config()
    
    @abstractmethod
    def get_default_model(self) -> str:
        """Return the default model for this provider"""
        pass
    
    @abstractmethod
    def _validate_config(self) -> None:
        """Validate API key and configuration"""
        pass
    
    @abstractmethod
    def generate(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: float = 0.7,
        **kwargs
    ) -> LLMResponse:
        """
        Generate text from a single prompt
        
        Args:
            prompt: Input text prompt
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature (0.0 to 1.0)
            **kwargs: Provider-specific parameters
            
        Returns:
            LLMResponse object with generated text and metadata
        """
        pass
    
    @abstractmethod
    def chat(
        self,
        messages: List[Message],
        max_tokens: Optional[int] = None,
        temperature: float = 0.7,
        **kwargs
    ) -> LLMResponse:
        """
        Multi-turn conversation interface
        
        Args:
            messages: List of Message objects (conversation history)
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            **kwargs: Provider-specific parameters
            
        Returns:
            LLMResponse object with assistant's reply
        """
        pass
    
    @abstractmethod
    def stream(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: float = 0.7,
        **kwargs
    ) -> Generator[str, None, None]:
        """
        Stream text generation token by token
        
        Args:
            prompt: Input text prompt
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            **kwargs: Provider-specific parameters
            
        Yields:
            Text chunks as they are generated
        """
        pass
    
    def count_tokens(self, text: str) -> int:
        """
        Estimate token count for text
        Default implementation (override for accurate counting)
        
        Args:
            text: Input text
            
        Returns:
            Estimated token count
        """
        # Rough estimation: ~4 characters per token
        return len(text) // 4
    
    def calculate_cost(self, input_tokens: int, output_tokens: int) -> float:
        """
        Calculate cost for API call
        
        Args:
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens
            
        Returns:
            Cost in USD
        """
        pricing = self.get_pricing()
        input_cost = (input_tokens / 1_000_000) * pricing['input_per_1m']
        output_cost = (output_tokens / 1_000_000) * pricing['output_per_1m']
        return input_cost + output_cost
    
    @abstractmethod
    def get_pricing(self) -> Dict[str, float]:
        """
        Return pricing information for current model
        
        Returns:
            Dict with 'input_per_1m' and 'output_per_1m' keys (USD)
        """
        pass
    
    def get_stats(self) -> Dict[str, Any]:
        """
        Get usage statistics for this client instance
        
        Returns:
            Dict with total tokens used and cost
        """
        return {
            'total_tokens': self.total_tokens,
            'total_cost_usd': self.total_cost,
            'model': self.model,
            'provider': self.__class__.__name__
        }
    
    def reset_stats(self) -> None:
        """Reset usage statistics"""
        self.total_tokens = 0
        self.total_cost = 0.0
        logger.info(f"Stats reset for {self.__class__.__name__}")
