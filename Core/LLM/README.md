# Multi-LLM Integration System

Unified Python framework for integrating Claude, ChatGPT, Gemini APIs and Local LLM into your AI applications.

## Features

✅ **Unified Interface** - Single API for all LLM providers  
✅ **Cost Tracking** - Automatic cost calculation and budgeting  
✅ **Intelligent Routing** - Cost-based and capability-based LLM selection  
✅ **Fallback Support** - Automatic failover between providers  
✅ **Streaming** - Real-time token streaming for all providers  
✅ **Local LLM** - Zero-cost local inference with Ollama  

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Keys

Copy `.env.template` to `.env` and add your API keys:

```bash
cp .env.template .env
```

Edit `.env`:
```env
ANTHROPIC_API_KEY=your_claude_key_here
OPENAI_API_KEY=your_openai_key_here
GOOGLE_API_KEY=your_gemini_key_here
```

### 3. Basic Usage

```python
from SDM_AI_PROJECT.Core.LLM import ClaudeClient, OpenAIClient, GeminiClient

# Use Claude
claude = ClaudeClient()
response = claude.generate("Explain quantum computing in simple terms")
print(response.content)
print(f"Cost: ${response.cost_usd:.4f}")

# Use OpenAI
openai = OpenAIClient()
response = openai.generate("Write a Python function to calculate fibonacci")
print(response.content)

# Use Gemini
gemini = GeminiClient()
response = gemini.generate("What are the benefits of renewable energy?")
print(response.content)
```

## Advanced Usage

### Multi-Turn Conversations

```python
from SDM_AI_PROJECT.Core.LLM import ClaudeClient, Message

client = ClaudeClient()

messages = [
    Message(role="system", content="You are a helpful coding assistant"),
    Message(role="user", content="How do I read a CSV file in Python?"),
]

response = client.chat(messages)
print(response.content)

# Continue conversation
messages.append(Message(role="assistant", content=response.content))
messages.append(Message(role="user", content="Can you show me with pandas?"))

response = client.chat(messages)
print(response.content)
```

### Streaming Responses

```python
from SDM_AI_PROJECT.Core.LLM import OpenAIClient

client = OpenAIClient()

print("Streaming response: ", end="")
for chunk in client.stream("Write a short story about a robot"):
    print(chunk, end="", flush=True)
print()
```

### Intelligent Routing

```python
from SDM_AI_PROJECT.Core.LLM import LLMRouter, TaskComplexity

router = LLMRouter()

# Simple task - uses local LLM (free)
client = router.select_by_cost(TaskComplexity.SIMPLE)
response = client.generate("What is 2+2?")

# Complex task - uses best model (Claude/GPT-4)
client = router.select_by_cost(TaskComplexity.COMPLEX)
response = client.generate("Explain the implications of Gödel's incompleteness theorems")

# Automatic fallback
response = router.generate_with_fallback(
    "Translate this to Korean: Hello, how are you?",
    preferred_providers=['claude', 'openai', 'gemini']
)
```

### Cost Tracking

```python
from SDM_AI_PROJECT.Core.LLM import ClaudeClient, get_tracker

# Initialize tracker with budget
tracker = get_tracker(
    budget_limit=50.0,  # $50 budget
    alert_threshold=10.0,  # Alert at $10
    export_dir="./cost_tracking"
)

# Use LLM
client = ClaudeClient()
response = client.generate("Explain machine learning")

# Track the cost
tracker.track(
    provider='claude',
    model=client.model,
    input_tokens=response.metadata['input_tokens'],
    output_tokens=response.metadata['output_tokens'],
    cost_usd=response.cost_usd,
    task_description="ML explanation"
)

# View summary
tracker.print_summary()

# Export data
tracker.export_to_csv()
tracker.export_to_json()
```

## Local LLM Setup

### Install Ollama

1. Download from https://ollama.ai/
2. Install and start Ollama
3. Pull a model:

```bash
ollama pull llama2
ollama pull mistral
ollama pull codellama
```

### Use Local LLM

```python
from SDM_AI_PROJECT.Core.LLM import LocalLLMClient

# Connect to Ollama
client = LocalLLMClient(model='llama2')

# List available models
models = client.list_models()
print(f"Available models: {models}")

# Generate (free!)
response = client.generate("Write a haiku about coding")
print(response.content)
print(f"Cost: ${response.cost_usd}")  # Always $0
```

## Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `ANTHROPIC_API_KEY` | Claude API key | - |
| `CLAUDE_DEFAULT_MODEL` | Default Claude model | `claude-3-5-sonnet-20241022` |
| `OPENAI_API_KEY` | OpenAI API key | - |
| `OPENAI_DEFAULT_MODEL` | Default OpenAI model | `gpt-4-turbo-preview` |
| `GOOGLE_API_KEY` | Gemini API key | - |
| `GEMINI_DEFAULT_MODEL` | Default Gemini model | `gemini-pro` |
| `OLLAMA_BASE_URL` | Ollama server URL | `http://localhost:11434` |
| `OLLAMA_DEFAULT_MODEL` | Default Ollama model | `llama2` |
| `DEFAULT_TEMPERATURE` | Sampling temperature | `0.7` |
| `DEFAULT_MAX_TOKENS` | Max output tokens | `2048` |

### Programmatic Configuration

```python
from SDM_AI_PROJECT.Core.LLM import get_config

config = get_config()

# Check which providers are configured
print(config.get_all_configured_providers())

# Validate all configurations
validation = config.validate_all()
print(validation)  # {'claude': True, 'openai': True, ...}
```

## Cost Comparison

| Provider | Model | Input (per 1M tokens) | Output (per 1M tokens) |
|----------|-------|----------------------|------------------------|
| Claude | Sonnet 3.5 | $3.00 | $15.00 |
| Claude | Opus | $15.00 | $75.00 |
| Claude | Haiku | $0.25 | $1.25 |
| OpenAI | GPT-4 Turbo | $10.00 | $30.00 |
| OpenAI | GPT-3.5 Turbo | $0.50 | $1.50 |
| Gemini | Pro | $0.50 | $1.50 |
| Local | Any | $0.00 | $0.00 |

## Architecture

```
SDM_AI_PROJECT/Core/LLM/
├── llm_client.py          # Base abstract client
├── config.py              # Configuration management
├── Clients/
│   ├── claude_client.py   # Claude implementation
│   ├── openai_client.py   # OpenAI implementation
│   ├── gemini_client.py   # Gemini implementation
│   └── local_llm_client.py # Local LLM implementation
└── Utils/
    ├── llm_router.py      # Intelligent routing
    └── cost_tracker.py    # Cost tracking
```

## Best Practices

### 1. Use Local LLM for Simple Tasks
```python
# Good: Use free local LLM for simple tasks
local = LocalLLMClient()
response = local.generate("Summarize this: ...")
```

### 2. Use Router for Automatic Selection
```python
# Good: Let router choose based on complexity
router = LLMRouter()
client = router.select_by_cost(TaskComplexity.MODERATE)
```

### 3. Always Track Costs
```python
# Good: Track all API calls
tracker = get_tracker(budget_limit=100.0)
# ... use LLMs ...
tracker.print_summary()
```

### 4. Implement Fallbacks
```python
# Good: Automatic fallback on failure
response = router.generate_with_fallback(
    prompt,
    preferred_providers=['claude', 'openai', 'local']
)
```

## Troubleshooting

### API Key Not Found
```
WARNING: No API key found for provider: claude
```
**Solution**: Add API key to `.env` file

### Ollama Connection Failed
```
WARNING: Could not connect to local LLM server
```
**Solution**: 
1. Install Ollama from https://ollama.ai/
2. Start Ollama service
3. Verify with `ollama list`

### Import Errors
```
ImportError: anthropic package not installed
```
**Solution**: `pip install -r requirements.txt`

## Future Enhancements

- [ ] Azure OpenAI support
- [ ] Anthropic function calling
- [ ] Token counting optimization
- [ ] Async/await support
- [ ] Caching layer
- [ ] Rate limiting

## License

Internal use for OPTIM SDM Agent project.
