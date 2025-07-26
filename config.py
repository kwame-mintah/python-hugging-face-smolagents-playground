from pydantic import Field
from pydantic_settings import BaseSettings


class EnvironmentVariables(BaseSettings):
    OLLAMA_BASE_API_URL: str = Field(
        description="The ollama server URL", default="http://localhost:11434"
    )
    OLLAMA_MODEL_NAME: str = Field(
        description="The Ollama model to be used for inference",
        default="ollama/mistral:7b",
    )
    AGENT_TASK: str = Field(
        description="The task the agent needs to complete",
        default="""
    Find me some restaurants to eat at tonight in London.
    Use web_search to get restaurant data.
    Authorized imports are: ['random', 'collections', 're', 'unicodedata', 'datetime',
    'queue', 'stat', 'time', 'math', 'statistics', 'itertools'].
    Code snippet should follow this regex pattern <code>(.*?)</code> 
    End your output after the final answer.
    """,
    )
    USE_HUGGING_FACE_INTERFACE: bool = Field(
        description="Whether to make a request to hugging face for model inference",
        default=False,
    )
    HUGGING_FACE_IMAGE_GENERATION_TOOL: str = Field(
        description="The name of the hugging face repository tool for text to image",
        default="m-ric/text-to-image",
    )
    HUGGING_FACE_INFERENCE_MODEL: str = Field(
        description="The name of the hugging face repository for model inference",
        default="Qwen/Qwen2.5-72B-Instruct",
    )


settings = EnvironmentVariables()
