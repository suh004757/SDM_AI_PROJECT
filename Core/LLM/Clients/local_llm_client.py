"""
Local LLM Client Implementation
Integrates with local LLM servers (Ollama, LM Studio)
"""

from typing import Optional, List, Generator, Dict, Any
import logging
import requests
import json

from ..llm_client import BaseLLMClient, LLMResponse, Message
from ..config import get_config

logger = logging.getLogger(__name__)


class LocalLLMClient(BaseLLMClient):
    """Local LLM client (Ollama/LM Studio) implementation"""
    
    def __init__(
        self,
        base_url: Optional[str] = None,
        model: Optional[str] = None,
        api_key: Optional[str] = None  # Not used, but kept for interface compatibility
    ):
        """
        Initialize Local LLM client
        
        Args:
            base_url: Base URL for local LLM server (e.g., http://localhost:11434)
            model: Model identifier (e.g., 'llama2', 'mistral')
            api_key: Not used for local LLM (kept for interface compatibility)
        """
        config = get_config()
        
        # Use provided base URL or load from config
        if base_url is None:
            base_url = config.ollama_base_url
        
        self.base_url = base_url.rstrip('/')
        
        # Use provided model or load from config
        if model is None:
            model = config.ollama_default_model
        
        super().__init__(api_key=None, model=model)
    
    def get_default_model(self) -> str:
        """Return default local model"""
        return 'llama2'
    
    def _validate_config(self) -> None:
        """Validate local LLM server connection"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            if response.status_code == 200:
                logger.info(f"Connected to local LLM server at {self.base_url}")
            else:
                logger.warning(f"Local LLM server returned status {response.status_code}")
        except requests.exceptions.RequestException as e:
            logger.warning(f"Could not connect to local LLM server at {self.base_url}: {e}")
    
    def generate(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: float = 0.7,
        **kwargs
    ) -> LLMResponse:
        """
        Generate text from prompt using local LLM
        
        Args:
            prompt: Input prompt
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            **kwargs: Additional parameters
            
        Returns:
            LLMResponse with generated text
        """
        try:
            # Prepare request
            payload = {
                'model': self.model,
                'prompt': prompt,
                'stream': False,
                'options': {
                    'temperature': temperature,
                }
            }
            
            if max_tokens:
                payload['options']['num_predict'] = max_tokens
            
            # Call local LLM API
            response = requests.post(
                f"{self.base_url}/api/generate",
                json=payload,
                timeout=120
            )
            response.raise_for_status()
            
            result = response.json()
            content = result.get('response', '')
            
            # Estimate tokens (local LLM may not provide exact counts)
            input_tokens = self.count_tokens(prompt)
            output_tokens = self.count_tokens(content)
            total_tokens = input_tokens + output_tokens
            
            # Update stats (no cost for local LLM)
            self.total_tokens += total_tokens
            
            return LLMResponse(
                content=content,
                model=self.model,
                provider='local',
                tokens_used=total_tokens,
                cost_usd=0.0,  # Local LLM is free
                finish_reason='stop',
                metadata={
                    'input_tokens': input_tokens,
                    'output_tokens': output_tokens,
                    'eval_count': result.get('eval_count'),
                    'eval_duration': result.get('eval_duration'),
                }
            )
            
        except Exception as e:
            logger.error(f"Local LLM error: {e}")
            raise
    
    def chat(
        self,
        messages: List[Message],
        max_tokens: Optional[int] = None,
        temperature: float = 0.7,
        **kwargs
    ) -> LLMResponse:
        """
        Multi-turn conversation with local LLM
        
        Args:
            messages: List of Message objects
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            **kwargs: Additional parameters
            
        Returns:
            LLMResponse with assistant's reply
        """
        try:
            # Convert messages to Ollama chat format
            ollama_messages = [
                {'role': msg.role, 'content': msg.content}
                for msg in messages
            ]
            
            # Prepare request
            payload = {
                'model': self.model,
                'messages': ollama_messages,
                'stream': False,
                'options': {
                    'temperature': temperature,
                }
            }
            
            if max_tokens:
                payload['options']['num_predict'] = max_tokens
            
            # Call local LLM API
            response = requests.post(
                f"{self.base_url}/api/chat",
                json=payload,
                timeout=120
            )
            response.raise_for_status()
            
            result = response.json()
            content = result.get('message', {}).get('content', '')
            
            # Estimate tokens
            input_tokens = sum(self.count_tokens(msg.content) for msg in messages)
            output_tokens = self.count_tokens(content)
            total_tokens = input_tokens + output_tokens
            
            # Update stats
            self.total_tokens += total_tokens
            
            return LLMResponse(
                content=content,
                model=self.model,
                provider='local',
                tokens_used=total_tokens,
                cost_usd=0.0,
                finish_reason='stop',
                metadata={
                    'input_tokens': input_tokens,
                    'output_tokens': output_tokens,
                }
            )
            
        except Exception as e:
            logger.error(f"Local LLM chat error: {e}")
            raise
    
    def stream(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: float = 0.7,
        **kwargs
    ) -> Generator[str, None, None]:
        """
        Stream text generation from local LLM
        
        Args:
            prompt: Input prompt
            max_tokens: Maximum tokens
            temperature: Sampling temperature
            **kwargs: Additional parameters
            
        Yields:
            Text chunks as they arrive
        """
        try:
            # Prepare request
            payload = {
                'model': self.model,
                'prompt': prompt,
                'stream': True,
                'options': {
                    'temperature': temperature,
                }
            }
            
            if max_tokens:
                payload['options']['num_predict'] = max_tokens
            
            # Stream response
            response = requests.post(
                f"{self.base_url}/api/generate",
                json=payload,
                stream=True,
                timeout=120
            )
            response.raise_for_status()
            
            for line in response.iter_lines():
                if line:
                    chunk = json.loads(line)
                    if 'response' in chunk:
                        yield chunk['response']
                        
        except Exception as e:
            logger.error(f"Local LLM streaming error: {e}")
            raise
    
    def get_pricing(self) -> Dict[str, float]:
        """Get pricing (always $0 for local LLM)"""
        return {
            'input_per_1m': 0.0,
            'output_per_1m': 0.0
        }
    
    def list_models(self) -> List[str]:
        """
        List available models on local LLM server
        
        Returns:
            List of model names
        """
        try:
            response = requests.get(f"{self.base_url}/api/tags")
            response.raise_for_status()
            result = response.json()
            return [model['name'] for model in result.get('models', [])]
        except Exception as e:
            logger.error(f"Error listing models: {e}")
            return []
    
    def pull_model(self, model_name: str) -> bool:
        """
        Pull/download a model to local LLM server
        
        Args:
            model_name: Name of model to pull (e.g., 'llama2', 'mistral')
            
        Returns:
            True if successful
        """
        try:
            logger.info(f"Pulling model {model_name}...")
            response = requests.post(
                f"{self.base_url}/api/pull",
                json={'name': model_name},
                stream=True,
                timeout=600
            )
            response.raise_for_status()
            
            # Stream progress
            for line in response.iter_lines():
                if line:
                    status = json.loads(line)
                    if 'status' in status:
                        logger.info(f"Pull status: {status['status']}")
            
            logger.info(f"Successfully pulled {model_name}")
            return True
            
        except Exception as e:
            logger.error(f"Error pulling model: {e}")
            return False
