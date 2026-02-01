"""
LLM Integration Package
Unified interface for Claude, OpenAI, Gemini, and Local LLM
"""

from .llm_client import BaseLLMClient, LLMResponse, Message
from .config import LLMConfig, get_config
from .Clients import ClaudeClient, OpenAIClient, GeminiClient, LocalLLMClient
from .Utils import LLMRouter, TaskComplexity, CostTracker, get_tracker

__version__ = '1.0.0'

__all__ = [
    # Base classes
    'BaseLLMClient',
    'LLMResponse',
    'Message',
    
    # Configuration
    'LLMConfig',
    'get_config',
    
    # Clients
    'ClaudeClient',
    'OpenAIClient',
    'GeminiClient',
    'LocalLLMClient',
    
    # Utilities
    'LLMRouter',
    'TaskComplexity',
    'CostTracker',
    'get_tracker',
]
