import logging
import os

import requests
from distutils.util import strtobool
from huggingface_hub import login
from smolagents import (
    load_tool,
    CodeAgent,
    InferenceClientModel,
    DuckDuckGoSearchTool,
    LiteLLMModel,
    FinalAnswerTool,
)

login(
    token=(os.getenv("HF_TOKEN") or os.getenv("HUGGING_FACE_TOKEN")), new_session=True
)
logger = logging.getLogger(__name__)

OLLAMA_BASE_API_URL = os.getenv("OLLAMA_BASE_API_URL", "http://localhost:11434")

def playground():
    """
    Initial playground to give the agent with a task and get a
    response.
    :return: Final result
    """
    if strtobool(os.getenv("USE_HUGGING_FACE_INTERFACE", False)):
        model = InferenceClientModel(model_id="Qwen/Qwen2.5-72B-Instruct")
        logger.info("Initialised model via hugging face, will incur costs")
    else:
        requests.get(url=OLLAMA_BASE_API_URL).raise_for_status()
        model = LiteLLMModel(
            model_id="ollama/llama3:instruct",
            api_base=OLLAMA_BASE_API_URL,
        )
        logger.info("Initialised model via Ollama, ensure model has been downloaded")

    image_generation_tool = load_tool(
        repo_id="m-ric/text-to-image", trust_remote_code=True
    )

    search_tool = DuckDuckGoSearchTool()
    final_answer_tool = FinalAnswerTool()

    agent = CodeAgent(
        tools=[image_generation_tool, search_tool, final_answer_tool], model=model
    )

    task = """
    Find me some restaurants to eat at tonight in London.
    Use web_search to get restaurant data.
    Summarize your findings using return_final_answer("...").
    Wrap your Python code in <code>...</code> tags only.
    End your output after the final answer.
    """

    result = agent.run(task=task, stream=False)

    return result


if __name__ == "__main__":
    playground()
