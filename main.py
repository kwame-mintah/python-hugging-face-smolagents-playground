import os

from huggingface_hub import login
from smolagents import load_tool, CodeAgent, InferenceClientModel, DuckDuckGoSearchTool

login(token=os.getenv("HUGGING_FACE_TOKEN"), new_session=True)


def playground():
    """
    Initial playground to give the agent with a task and get a
    response.
    :return: Final result
    """
    image_generation_tool = load_tool(
        repo_id="m-ric/text-to-image", trust_remote_code=True
    )

    search_tool = DuckDuckGoSearchTool()

    model = InferenceClientModel(model_id="Qwen/Qwen2.5-72B-Instruct")

    agent = CodeAgent(tools=[image_generation_tool, search_tool], model=model)

    result = agent.run(
        task="Find me some restaurants to eat at tonight in london", stream=False
    )

    return result


if __name__ == "__main__":
    playground()
