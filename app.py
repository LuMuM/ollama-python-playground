from openai import AsyncOpenAI
import chainlit as cl

client = AsyncOpenAI(base_url = "http://localhost:11434/v1", api_key= "nokeyneeded")
cl.instrument_openai()

settings = {
    "model" : "phi3:mini", 
    "temperature": 0,
    "n": 1
}


@cl.on_message
async def on_message(message: cl.Message):
    response = await client.chat.completions.create(
        messages=[
            {
                "content": "You are a helpful bot, you always reply in Spanish",
                "role": "system"
            },
            {
                "content": message.content,
                "role": "user"
            }
        ],
        **settings
    )
    await  cl.Message(content=response.choices[0].message.content).send()
