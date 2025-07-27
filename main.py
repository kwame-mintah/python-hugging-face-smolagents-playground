import logging
import os
import sys

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
logger.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


OLLAMA_BASE_API_URL = os.getenv("OLLAMA_BASE_API_URL", "http://localhost:11434")

def playground():
    """
    Initial playground to give the agent with a task and get a
    response.
    :return: Final result
    """

    logger.info("hello world")
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

    search_tool = DuckDuckGoSearchTool()
    final_answer_tool = FinalAnswerTool()

    instructions = """ 
    You are an expert Product Manager who excels in writing well structured and clear requirements for software projects.
    Your input will be a high level ideas for a software project and lay out a detailed requirements for how to create this software using best practises.
    Use web_search to find examples of good requirements if you need.
    You output will only be text.


    """

    agent = CodeAgent(
        tools=[search_tool, final_answer_tool], model=model, instructions=instructions
    )

    task = """
    Create a TODO web application
    Output your findings using return_final_answer("...").
    Wrap your Python code in <code>...</code> tags only.
    End your output after the final answer.
    """

    result = agent.run(task=task, stream=False)
    
    logger.info(f"{result}")

    return result


if __name__ == "__main__":
    playground()
