import logging
import os

import requests
from huggingface_hub import login
from smolagents import (
    load_tool,
    CodeAgent,
    InferenceClientModel,
    DuckDuckGoSearchTool,
    LiteLLMModel,
)

login(token=os.getenv("HUGGING_FACE_TOKEN"), new_session=True)
logger = logging.getLogger(__name__)

OLLAMA_BASE_API_URL = os.getenv("OLLAMA_BASE_API_URL", "http://localhost:11434")

def playground():
    """
    Initial playground to give the agent with a task and get a
    response.
    :return: Final result
    """
    if os.getenv("USE_HUGGING_FACE_INTERFACE", False):
        model = InferenceClientModel(model_id="Qwen/Qwen2.5-72B-Instruct")
        logger.info("Initialised model via hugging face, will incur costs")
    else:
        requests.get(url=OLLAMA_BASE_API_URL).raise_for_status()
        model = LiteLLMModel(
            model_id="ollama/Qwen2.5:7B-instruct",
            api_base=OLLAMA_BASE_API_URL,
        )
        logger.info("Initialised model via Ollama, ensure model has been downloaded")

    image_generation_tool = load_tool(
        repo_id="m-ric/text-to-image", trust_remote_code=True
    )

    search_tool = DuckDuckGoSearchTool()

    agent = CodeAgent(tools=[image_generation_tool, search_tool], model=model)

    result = agent.run(
        task="Find me some restaurants to eat at tonight in london", stream=False
    )

    return result


if __name__ == "__main__":
    playground()
