# 🛝 Hugging face smolagents playground

![python](https://img.shields.io/badge/python-3.12.0-informational)

As the name of the repository suggests, it's just a [
_playground_](https://dictionary.cambridge.org/dictionary/english/playground). A place to better understand Hugging
Face [smolagents](https://huggingface.co/docs/smolagents/index)
and how it can be utilised for various tasks and create a multi-agent workflow.

## Prerequisites

1. [Docker for desktop](https://docs.docker.com/desktop/)
2. [Ollama](https://ollama.com/download)
3. [uv](https://docs.astral.sh/uv/#installation)

### Usage via `pip`

1. Install python packages used for the project

```pycon
pip install -r requirements.txt
```

2. Run the application

```pycon
python main.py
```

### Usage via `uv`

1. Install python packages used for the project

```pycon
uv sync
```

2. Run the application

```pycon
uv run main.py
```

## Environment variables

The following environment variables are used by this project.

| Environment Variable               | Description                                                    | Default Value                            |
| ---------------------------------- | -------------------------------------------------------------- | ---------------------------------------- |
| AGENT_TASK                         | The task the agent needs to complete                           | Create a hello world app, using FastAPI. |
| LLM_PROVIDER                       | The inference model provider to use                            | ollama                                   |
| OLLAMA_BASE_API_URL                | The ollama server URL                                          | http://localhost:11434                   |
| OLLAMA_MODEL_NAME                  | The Ollama model to be used for inference                      | ollama/mistral:7b                        |
| GOOGLE_API_KEY                     | Your Google Gemini API key                                     |                                          |
| GOOGLE_GEMINI_LLM_MODEL            | The Gemini model to use                                        | gemini-2.5-flash                         |
| HUGGING_FACE_IMAGE_GENERATION_TOOL | The name of the hugging face repository tool for text to image | m-ric/text-to-image                      |
| HUGGING_FACE_INFERENCE_MODEL       | The name of the hugging face repository for model inference    | Qwen/Qwen2.5-72B-Instruct                |
