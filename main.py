import openai
import asyncio
import os

from openai import OpenAI
from openai import AsyncOpenAI
from dotenv import load_dotenv


# secrets for API keys
env_path = os.path.join(os.path.dirname(__file__), '..', 'secrets', '.env')
load_dotenv(env_path)


client = AsyncOpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=os.environ.get("OPENAI_API_KEY"),
)

async def main() -> None:
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Say this is a test",
            }
        ],
        model="gpt-3.5-turbo",
    )


asyncio.run(main())