from typing import Iterator
import openai


MODEL = "llama-3.2-1b-instruct"
TEMPERATURE = 0.7

client = openai.OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="***",
)


def generate_response(
    messages: list[dict], temperature: float = TEMPERATURE, model: str = MODEL
) -> str:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message.content


def stream_response(
    messages: list[dict], temperature: float = TEMPERATURE, model: str = MODEL
) -> Iterator[str]:
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
        temperature=temperature,
    )
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content
