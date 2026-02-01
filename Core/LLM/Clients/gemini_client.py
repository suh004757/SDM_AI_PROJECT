"""
Google Gemini API Client Implementation
Integrates with Google's Gemini models
"""

from typing import Optional, List, Generator, Dict, Any
import logging

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    logging.warning("google-generativeai package not installed. Install with: pip install google-generativeai")

from ..llm_client import BaseLLMClient, LLMResponse, Message
from ..config import get_config

logger = logging.getLogger(__name__)


class GeminiClient(BaseLLMClient):
    """Google Gemini API client implementation"""
    
    # Pricing as of 2026 (USD per 1M tokens)
    PRICING = {
        'gemini-pro': {'input_per_1m': 0.5, 'output_per_1m': 1.5},
        'gemini-ultra': {'input_per_1m': 10.0, 'output_per_1m': 30.0},
        'gemini-1.5-pro': {'input_per_1m': 3.5, 'output_per_1m': 10.5},
    }
    
    def __init__(self, api_key: Optional[str] = None, model: Optional[str] = None):
        """
        Initialize Gemini client
        
        Args:
            api_key: Google API key (if None, loads from config)
            model: Model identifier (if None, uses default from config)
        """
        if not GEMINI_AVAILABLE:
            raise ImportError("google-generativeai package required. Install with: pip install google-generativeai")
        
        config = get_config()
        
        # Use provided API key or load from config
        if api_key is None:
            api_key = config.google_api_key
        
        # Use provided model or load from config
        if model is None:
            model = config.gemini_default_model
        
        super().__init__(api_key=api_key, model=model)
        
        # Configure Gemini
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.client = genai.GenerativeModel(self.model)
        else:
            self.client = None
            logger.warning("Gemini client initialized without API key - will fail on actual calls")
    
    def get_default_model(self) -> str:
        """Return default Gemini model"""
        return 'gemini-pro'
    
    def _validate_config(self) -> None:
        """Validate API key"""
        if not self.api_key:
            logger.warning("No API key provided for Gemini client")
    
    def generate(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: float = 0.7,
        **kwargs
    ) -> LLMResponse:
        """
        Generate text from prompt using Gemini
        
        Args:
            prompt: Input prompt
            max_tokens: Maximum tokens to generate (default: 2048)
            temperature: Sampling temperature
            **kwargs: Additional Gemini-specific parameters
            
        Returns:
            LLMResponse with generated text
        """
        if not self.client:
            raise ValueError("Gemini client not initialized with API key")
        
        try:
            # Configure generation
            generation_config = {
                'temperature': temperature,
            }
            if max_tokens:
                generation_config['max_output_tokens'] = max_tokens
            
            # Call Gemini API
            response = self.client.generate_content(
                prompt,
                generation_config=generation_config,
                **kwargs
            )
            
            # Extract response
            content = response.text
            
            # Gemini doesn't always provide token counts
            # Estimate if not available
            input_tokens = self.count_tokens(prompt)
            output_tokens = self.count_tokens(content)
            total_tokens = input_tokens + output_tokens
            
            # Calculate cost
            cost = self.calculate_cost(input_tokens, output_tokens)
            
            # Update stats
            self.total_tokens += total_tokens
            self.total_cost += cost
            
            return LLMResponse(
                content=content,
                model=self.model,
                provider='gemini',
                tokens_used=total_tokens,
                cost_usd=cost,
                finish_reason=response.candidates[0].finish_reason.name if response.candidates else None,
                metadata={
                    'input_tokens': input_tokens,
                    'output_tokens': output_tokens,
                    'safety_ratings': [
                        {
                            'category': rating.category.name,
                            'probability': rating.probability.name
                        }
                        for rating in response.candidates[0].safety_ratings
                    ] if response.candidates else []
                }
            )
            
        except Exception as e:
            logger.error(f"Gemini API error: {e}")
            raise
    
    def chat(
        self,
        messages: List[Message],
        max_tokens: Optional[int] = None,
        temperature: float = 0.7,
        **kwargs
    ) -> LLMResponse:
        """
        Multi-turn conversation with Gemini
        
        Args:
            messages: List of Message objects
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            **kwargs: Additional parameters
            
        Returns:
            LLMResponse with assistant's reply
        """
        if not self.client:
            raise ValueError("Gemini client not initialized with API key")
        
        try:
            # Start chat session
            chat = self.client.start_chat(history=[])
            
            # Configure generation
            generation_config = {
                'temperature': temperature,
            }
            if max_tokens:
                generation_config['max_output_tokens'] = max_tokens
            
            # Convert messages to Gemini format and send
            # Gemini uses 'user' and 'model' roles
            for msg in messages[:-1]:  # All but last message
                role = 'model' if msg.role == 'assistant' else 'user'
                chat.history.append({
                    'role': role,
                    'parts': [msg.content]
                })
            
            # Send last message and get response
            last_msg = messages[-1]
            response = chat.send_message(
                last_msg.content,
                generation_config=generation_config,
                **kwargs
            )
            
            # Extract response
            content = response.text
            
            # Estimate tokens
            input_tokens = sum(self.count_tokens(msg.content) for msg in messages)
            output_tokens = self.count_tokens(content)
            total_tokens = input_tokens + output_tokens
            
            # Calculate cost
            cost = self.calculate_cost(input_tokens, output_tokens)
            
            # Update stats
            self.total_tokens += total_tokens
            self.total_cost += cost
            
            return LLMResponse(
                content=content,
                model=self.model,
                provider='gemini',
                tokens_used=total_tokens,
                cost_usd=cost,
                finish_reason=response.candidates[0].finish_reason.name if response.candidates else None,
                metadata={
                    'input_tokens': input_tokens,
                    'output_tokens': output_tokens,
                }
            )
            
        except Exception as e:
            logger.error(f"Gemini chat error: {e}")
            raise
    
    def stream(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: float = 0.7,
        **kwargs
    ) -> Generator[str, None, None]:
        """
        Stream text generation from Gemini
        
        Args:
            prompt: Input prompt
            max_tokens: Maximum tokens
            temperature: Sampling temperature
            **kwargs: Additional parameters
            
        Yields:
            Text chunks as they arrive
        """
        if not self.client:
            raise ValueError("Gemini client not initialized with API key")
        
        try:
            # Configure generation
            generation_config = {
                'temperature': temperature,
            }
            if max_tokens:
                generation_config['max_output_tokens'] = max_tokens
            
            # Stream response
            response = self.client.generate_content(
                prompt,
                generation_config=generation_config,
                stream=True,
                **kwargs
            )
            
            for chunk in response:
                if chunk.text:
                    yield chunk.text
                    
        except Exception as e:
            logger.error(f"Gemini streaming error: {e}")
            raise
    
    def get_pricing(self) -> Dict[str, float]:
        """Get pricing for current model"""
        return self.PRICING.get(
            self.model,
            {'input_per_1m': 0.5, 'output_per_1m': 1.5}  # Default to Gemini Pro pricing
        )
