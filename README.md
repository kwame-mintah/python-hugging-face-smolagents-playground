# 🛝 Hugging face smolagents playground

![python](https://img.shields.io/badge/python-3.12.0-informational)

As the name of the repository suggests, it's just a [
_playground_](https://dictionary.cambridge.org/dictionary/english/playground). A place to better understand Hugging
Face [smolagents](https://huggingface.co/docs/smolagents/index)
and how it can be utilised for various tasks and create a multi-agent workflow.

## Prerequisites

1. [Docker for desktop](https://docs.docker.com/desktop/)
2. [Ollama](https://ollama.com/download)

# Usage

1. Install python packages used for the project

```pycon
pip install -r requirements.txt
```

## Environment variables

The following environment variables are used by this project.

| Environment Variable | Description                                                   | Default Value |
|----------------------|---------------------------------------------------------------|---------------|
| HUGGING_FACE_TOKEN   | The token to identify you on [hf.co](https://huggingface.co/) |               |
