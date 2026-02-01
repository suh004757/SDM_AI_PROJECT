"""
Usage Examples for Multi-LLM Integration
Demonstrates all major features and use cases
"""

import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(project_root))

from SDM_AI_PROJECT.Core.LLM import (
    ClaudeClient, OpenAIClient, GeminiClient, LocalLLMClient,
    LLMRouter, TaskComplexity,
    CostTracker, get_tracker,
    Message
)


def example_1_basic_generation():
    """Example 1: Basic text generation with each provider"""
    print("\n" + "="*60)
    print("EXAMPLE 1: Basic Text Generation")
    print("="*60)
    
    prompt = "Explain what an API is in one sentence."
    
    # Note: These will only work if API keys are configured
    try:
        print("\n--- Claude ---")
        claude = ClaudeClient()
        response = claude.generate(prompt, max_tokens=100)
        print(f"Response: {response.content}")
        print(f"Tokens: {response.tokens_used}, Cost: ${response.cost_usd:.4f}")
    except Exception as e:
        print(f"Claude not available: {e}")
    
    try:
        print("\n--- OpenAI ---")
        openai = OpenAIClient()
        response = openai.generate(prompt, max_tokens=100)
        print(f"Response: {response.content}")
        print(f"Tokens: {response.tokens_used}, Cost: ${response.cost_usd:.4f}")
    except Exception as e:
        print(f"OpenAI not available: {e}")
    
    try:
        print("\n--- Gemini ---")
        gemini = GeminiClient()
        response = gemini.generate(prompt, max_tokens=100)
        print(f"Response: {response.content}")
        print(f"Tokens: {response.tokens_used}, Cost: ${response.cost_usd:.4f}")
    except Exception as e:
        print(f"Gemini not available: {e}")
    
    try:
        print("\n--- Local LLM (Free!) ---")
        local = LocalLLMClient()
        response = local.generate(prompt, max_tokens=100)
        print(f"Response: {response.content}")
        print(f"Tokens: {response.tokens_used}, Cost: ${response.cost_usd:.4f}")
    except Exception as e:
        print(f"Local LLM not available: {e}")


def example_2_chat_conversation():
    """Example 2: Multi-turn conversation"""
    print("\n" + "="*60)
    print("EXAMPLE 2: Multi-Turn Conversation")
    print("="*60)
    
    try:
        client = ClaudeClient()
        
        messages = [
            Message(role="system", content="You are a helpful Python tutor"),
            Message(role="user", content="How do I read a JSON file in Python?"),
        ]
        
        print("\nUser: How do I read a JSON file in Python?")
        response = client.chat(messages, max_tokens=200)
        print(f"\nAssistant: {response.content}")
        
        # Continue conversation
        messages.append(Message(role="assistant", content=response.content))
        messages.append(Message(role="user", content="Can you show me error handling too?"))
        
        print("\nUser: Can you show me error handling too?")
        response = client.chat(messages, max_tokens=200)
        print(f"\nAssistant: {response.content}")
        
        print(f"\nTotal cost: ${response.cost_usd:.4f}")
        
    except Exception as e:
        print(f"Error: {e}")


def example_3_streaming():
    """Example 3: Streaming responses"""
    print("\n" + "="*60)
    print("EXAMPLE 3: Streaming Responses")
    print("="*60)
    
    try:
        client = OpenAIClient()
        
        prompt = "Write a short haiku about artificial intelligence"
        
        print(f"\nPrompt: {prompt}")
        print("\nStreaming response: ", end="", flush=True)
        
        for chunk in client.stream(prompt, max_tokens=100):
            print(chunk, end="", flush=True)
        
        print("\n")
        
    except Exception as e:
        print(f"Error: {e}")


def example_4_intelligent_routing():
    """Example 4: Intelligent LLM routing"""
    print("\n" + "="*60)
    print("EXAMPLE 4: Intelligent Routing")
    print("="*60)
    
    try:
        router = LLMRouter()
        
        print(f"\nAvailable providers: {router.get_available_providers()}")
        
        # Simple task - use local LLM
        print("\n--- Simple Task (uses local LLM) ---")
        client = router.select_by_cost(TaskComplexity.SIMPLE, prefer_local=True)
        response = client.generate("What is 5 + 7?", max_tokens=50)
        print(f"Response: {response.content}")
        print(f"Provider: {response.provider}, Cost: ${response.cost_usd:.4f}")
        
        # Moderate task - use cheaper cloud model
        print("\n--- Moderate Task (uses cost-effective cloud) ---")
        client = router.select_by_cost(TaskComplexity.MODERATE)
        response = client.generate("Explain the water cycle", max_tokens=150)
        print(f"Response: {response.content[:100]}...")
        print(f"Provider: {response.provider}, Cost: ${response.cost_usd:.4f}")
        
        # Complex task - use best model
        print("\n--- Complex Task (uses best model) ---")
        client = router.select_by_cost(TaskComplexity.COMPLEX)
        response = client.generate(
            "Explain the philosophical implications of artificial consciousness",
            max_tokens=200
        )
        print(f"Response: {response.content[:100]}...")
        print(f"Provider: {response.provider}, Cost: ${response.cost_usd:.4f}")
        
    except Exception as e:
        print(f"Error: {e}")


def example_5_fallback_handling():
    """Example 5: Automatic fallback on failure"""
    print("\n" + "="*60)
    print("EXAMPLE 5: Automatic Fallback")
    print("="*60)
    
    try:
        router = LLMRouter()
        
        prompt = "Translate to Korean: Hello, how are you today?"
        
        # Try providers in order, automatically fallback on failure
        response = router.generate_with_fallback(
            prompt,
            preferred_providers=['claude', 'openai', 'gemini', 'local'],
            max_tokens=100
        )
        
        print(f"\nPrompt: {prompt}")
        print(f"Response: {response.content}")
        print(f"Provider used: {response.provider}")
        print(f"Cost: ${response.cost_usd:.4f}")
        
    except Exception as e:
        print(f"All providers failed: {e}")


def example_6_cost_tracking():
    """Example 6: Cost tracking and budgeting"""
    print("\n" + "="*60)
    print("EXAMPLE 6: Cost Tracking")
    print("="*60)
    
    try:
        # Initialize tracker with budget
        tracker = get_tracker(
            budget_limit=1.0,  # $1 budget
            alert_threshold=0.5,  # Alert at $0.50
            export_dir="./cost_tracking"
        )
        
        # Make several API calls
        client = ClaudeClient()
        
        for i in range(3):
            response = client.generate(
                f"Generate a random fact about science #{i+1}",
                max_tokens=100
            )
            
            # Track the cost
            tracker.track(
                provider='claude',
                model=client.model,
                input_tokens=response.metadata['input_tokens'],
                output_tokens=response.metadata['output_tokens'],
                cost_usd=response.cost_usd,
                task_description=f"Science fact #{i+1}"
            )
        
        # Print summary
        tracker.print_summary()
        
        # Export data
        csv_path = tracker.export_to_csv()
        print(f"\nExported to: {csv_path}")
        
        # Get provider-specific stats
        claude_stats = tracker.get_provider_stats('claude')
        print(f"\nClaude stats: {claude_stats}")
        
    except Exception as e:
        print(f"Error: {e}")


def example_7_local_llm_management():
    """Example 7: Local LLM model management"""
    print("\n" + "="*60)
    print("EXAMPLE 7: Local LLM Management")
    print("="*60)
    
    try:
        client = LocalLLMClient()
        
        # List available models
        models = client.list_models()
        print(f"\nAvailable models: {models}")
        
        # Use a specific model
        if models:
            client.model = models[0]
            response = client.generate("Write a one-line joke", max_tokens=50)
            print(f"\nJoke: {response.content}")
            print(f"Model: {response.model}, Cost: ${response.cost_usd}")
        
        # Pull a new model (commented out - takes time)
        # print("\nPulling 'mistral' model...")
        # success = client.pull_model('mistral')
        # print(f"Pull successful: {success}")
        
    except Exception as e:
        print(f"Error: {e}")


def example_8_combined_workflow():
    """Example 8: Complete workflow with routing and tracking"""
    print("\n" + "="*60)
    print("EXAMPLE 8: Complete Workflow")
    print("="*60)
    
    try:
        # Initialize router and tracker
        router = LLMRouter()
        tracker = get_tracker(budget_limit=5.0)
        
        # Define tasks with different complexities
        tasks = [
            ("What is 2+2?", TaskComplexity.SIMPLE),
            ("Explain photosynthesis briefly", TaskComplexity.MODERATE),
            ("Analyze the economic impact of AI on employment", TaskComplexity.COMPLEX),
        ]
        
        for prompt, complexity in tasks:
            print(f"\n--- Task: {prompt} ---")
            print(f"Complexity: {complexity.value}")
            
            # Select appropriate LLM
            client = router.select_by_cost(complexity)
            
            # Generate response
            response = client.generate(prompt, max_tokens=150)
            
            # Track cost
            tracker.track(
                provider=response.provider,
                model=response.model,
                input_tokens=response.metadata.get('input_tokens', 0),
                output_tokens=response.metadata.get('output_tokens', 0),
                cost_usd=response.cost_usd,
                task_description=prompt
            )
            
            print(f"Provider: {response.provider}")
            print(f"Response: {response.content[:100]}...")
            print(f"Cost: ${response.cost_usd:.4f}")
        
        # Final summary
        print("\n" + "="*60)
        tracker.print_summary()
        
        # Get router stats
        router_stats = router.get_total_stats()
        print(f"\nRouter total stats: {router_stats}")
        
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Run all examples"""
    print("\n" + "="*60)
    print("MULTI-LLM INTEGRATION EXAMPLES")
    print("="*60)
    print("\nNote: Some examples require API keys to be configured")
    print("Configure API keys in .env file (see .env.template)")
    
    # Run examples
    example_1_basic_generation()
    example_2_chat_conversation()
    example_3_streaming()
    example_4_intelligent_routing()
    example_5_fallback_handling()
    example_6_cost_tracking()
    example_7_local_llm_management()
    example_8_combined_workflow()
    
    print("\n" + "="*60)
    print("ALL EXAMPLES COMPLETED")
    print("="*60)


if __name__ == "__main__":
    main()
