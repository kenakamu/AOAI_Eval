#https://github.com/MicrosoftDocs/azure-ai-docs/blob/main/articles/ai-studio/how-to/develop/simulator-interaction-data.md

from azure.ai.evaluation.simulator import Simulator
import asyncio
import wikipedia
import os
from typing import List, Dict, Any, Optional
from promptflow.client import load_flow
import json
from dotenv import load_dotenv 
load_dotenv() 

azure_openai_endpoint = os.environ.get("AZURE_OPENAI_ENDPOINT")
azure_openai_deployment = os.environ.get("AZURE_OPENAI_DEPLOYMENT")
azure_openai_api_version = os.environ.get("AZURE_OPENAI_API_VERSION")

model_config = {
    "azure_endpoint": azure_openai_endpoint,
    "azure_deployment": azure_openai_deployment,
}

conversation_turns = []

async def callback( # callback will generate assistant response
    messages: List[Dict],
    stream: bool = False,
    session_state: Any = None,  # noqa: ANN401
    context: Optional[Dict[str, Any]] = None,
) -> dict:
    messages_list = messages["messages"]
    # Get the last message
    latest_message = messages_list[-1]
    query = latest_message["content"]
    context = latest_message.get("context", None) # looks for context, default None
    # Call your endpoint or AI application here
    current_dir = os.path.dirname(__file__)
    prompty_path = os.path.join(current_dir, "application.prompty")
    _flow = load_flow(source=prompty_path, model={"configuration": model_config })
    response = _flow(query=query, context=context, conversation_history=messages_list)
    # Format the response to follow the OpenAI chat protocol
    formatted_response = {
        "content": response,
        "role": "assistant",
        "context": context,
    }
    messages["messages"].append(formatted_response)
    return {
        "messages": messages["messages"],
        "stream": stream,
        "session_state": session_state,
        "context": context
    }
   

async def main() -> None:
    # Prepare the text to send to the simulator
    wiki_search_term = "Leonardo da vinci"
    wiki_title = wikipedia.search(wiki_search_term)[0]
    wiki_page = wikipedia.page(wiki_title)
    text = wiki_page.summary[:5000]
    conversation_turns.append(["how are you doing today?"])
    simulator = Simulator(model_config=model_config) # simulator generates user input

    # outputs = await simulator(
    #     target=callback,
    #     conversation_turns=conversation_turns,
    #     max_conversation_turns=3,
    # )

    outputs = await simulator(
        target=callback,
        text=text,
        num_queries=4,
        tasks=[
            f"I am a student and I want to learn more about {wiki_search_term}",
            f"I am a teacher and I want to teach my students about {wiki_search_term}",
            f"I am a researcher and I want to do a detailed research on {wiki_search_term}",
            f"I am a statistician and I want to do a detailed table of factual data concerning {wiki_search_term}",
        ],
    )

    print(json.dumps(outputs, indent=2))

if __name__ == '__main__':
    asyncio.run(main())