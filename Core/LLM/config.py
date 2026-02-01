"""
Configuration Management for LLM Integration
Handles API keys, environment variables, and default settings
"""

import os
from typing import Optional, Dict, Any
from pathlib import Path
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)


class LLMConfig:
    """Centralized configuration for all LLM providers"""
    
    def __init__(self, env_file: Optional[str] = None):
        """
        Initialize configuration
        
        Args:
            env_file: Path to .env file (defaults to project root)
        """
        # Load environment variables
        if env_file:
            load_dotenv(env_file)
        else:
            # Try to find .env in project root
            project_root = Path(__file__).parent.parent.parent.parent
            env_path = project_root / '.env'
            if env_path.exists():
                load_dotenv(env_path)
                logger.info(f"Loaded environment from {env_path}")
            else:
                logger.warning(f"No .env file found at {env_path}")
        
        self._load_config()
    
    def _load_config(self) -> None:
        """Load configuration from environment variables"""
        
        # Claude (Anthropic)
        self.anthropic_api_key = os.getenv('ANTHROPIC_API_KEY')
        self.claude_default_model = os.getenv('CLAUDE_DEFAULT_MODEL', 'claude-3-5-sonnet-20241022')
        
        # OpenAI
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.openai_default_model = os.getenv('OPENAI_DEFAULT_MODEL', 'gpt-4-turbo-preview')
        
        # Google Gemini
        self.google_api_key = os.getenv('GOOGLE_API_KEY')
        self.gemini_default_model = os.getenv('GEMINI_DEFAULT_MODEL', 'gemini-pro')
        
        # Local LLM (Ollama)
        self.ollama_base_url = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
        self.ollama_default_model = os.getenv('OLLAMA_DEFAULT_MODEL', 'llama2')
        
        # General settings
        self.default_temperature = float(os.getenv('DEFAULT_TEMPERATURE', '0.7'))
        self.default_max_tokens = int(os.getenv('DEFAULT_MAX_TOKENS', '2048'))
        self.enable_cost_tracking = os.getenv('ENABLE_COST_TRACKING', 'true').lower() == 'true'
        self.cost_alert_threshold = float(os.getenv('COST_ALERT_THRESHOLD', '10.0'))
    
    def get_api_key(self, provider: str) -> Optional[str]:
        """
        Get API key for specific provider
        
        Args:
            provider: Provider name ('claude', 'openai', 'gemini')
            
        Returns:
            API key or None if not configured
        """
        key_map = {
            'claude': self.anthropic_api_key,
            'anthropic': self.anthropic_api_key,
            'openai': self.openai_api_key,
            'gpt': self.openai_api_key,
            'gemini': self.google_api_key,
            'google': self.google_api_key,
        }
        
        key = key_map.get(provider.lower())
        if not key:
            logger.warning(f"No API key found for provider: {provider}")
        return key
    
    def get_default_model(self, provider: str) -> str:
        """
        Get default model for provider
        
        Args:
            provider: Provider name
            
        Returns:
            Default model identifier
        """
        model_map = {
            'claude': self.claude_default_model,
            'anthropic': self.claude_default_model,
            'openai': self.openai_default_model,
            'gpt': self.openai_default_model,
            'gemini': self.gemini_default_model,
            'google': self.gemini_default_model,
            'ollama': self.ollama_default_model,
            'local': self.ollama_default_model,
        }
        
        return model_map.get(provider.lower(), 'unknown')
    
    def is_configured(self, provider: str) -> bool:
        """
        Check if provider is properly configured
        
        Args:
            provider: Provider name
            
        Returns:
            True if API key exists (or not needed for local)
        """
        if provider.lower() in ['ollama', 'local']:
            return True  # Local LLM doesn't need API key
        
        return self.get_api_key(provider) is not None
    
    def get_all_configured_providers(self) -> list[str]:
        """
        Get list of all configured providers
        
        Returns:
            List of provider names that have API keys
        """
        providers = []
        
        if self.anthropic_api_key:
            providers.append('claude')
        if self.openai_api_key:
            providers.append('openai')
        if self.google_api_key:
            providers.append('gemini')
        
        # Local LLM is always "configured" (doesn't need API key)
        providers.append('ollama')
        
        return providers
    
    def validate_all(self) -> Dict[str, bool]:
        """
        Validate all provider configurations
        
        Returns:
            Dict mapping provider names to validation status
        """
        return {
            'claude': self.is_configured('claude'),
            'openai': self.is_configured('openai'),
            'gemini': self.is_configured('gemini'),
            'ollama': True,  # Always available
        }
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Export configuration as dictionary (without exposing API keys)
        
        Returns:
            Configuration dictionary
        """
        return {
            'providers': {
                'claude': {
                    'configured': bool(self.anthropic_api_key),
                    'default_model': self.claude_default_model,
                },
                'openai': {
                    'configured': bool(self.openai_api_key),
                    'default_model': self.openai_default_model,
                },
                'gemini': {
                    'configured': bool(self.google_api_key),
                    'default_model': self.gemini_default_model,
                },
                'ollama': {
                    'configured': True,
                    'base_url': self.ollama_base_url,
                    'default_model': self.ollama_default_model,
                },
            },
            'settings': {
                'default_temperature': self.default_temperature,
                'default_max_tokens': self.default_max_tokens,
                'enable_cost_tracking': self.enable_cost_tracking,
                'cost_alert_threshold': self.cost_alert_threshold,
            }
        }


# Global configuration instance
_config_instance = None


def get_config(env_file: Optional[str] = None) -> LLMConfig:
    """
    Get global configuration instance (singleton pattern)
    
    Args:
        env_file: Path to .env file (only used on first call)
        
    Returns:
        LLMConfig instance
    """
    global _config_instance
    if _config_instance is None:
        _config_instance = LLMConfig(env_file)
    return _config_instance
