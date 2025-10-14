from pydantic import Field
from pydantic_settings import BaseSettings


class EnvironmentVariables(BaseSettings):
    AGENT_TASK: str = Field(
        description="The task the agent needs to complete",
        default="Create a hello world app, using FastAPI.",
    )
    LLM_INFERENCE_PROVIDER: str = Field(
        description="The inference model provider to use",
        default="ollama",
    )
    OLLAMA_BASE_API_URL: str = Field(
        description="The ollama server URL", default="http://localhost:11434"
    )
    OLLAMA_MODEL_NAME: str = Field(
        description="The Ollama model to be used for inference",
        default="ollama/mistral:7b",
    )
    GOOGLE_GEMINI_API_KEY: str = Field(
        description="Your Google Gemini API key", alias="GOOGLE_API_KEY", default=""
    )
    GOOGLE_GEMINI_LLM_MODEL: str = Field(
        description="The Gemini model to use", default="gemini-2.5-flash"
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
