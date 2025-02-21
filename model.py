import openai
from typing import Optional

# Configure OpenAI client
client = openai.OpenAI(api_key="no-key", base_url="http://localhost:1234/v1")

model_name = "deepseek-r1-distill-qwen-7b"


def get_ai_response(prompt: str, model: str = model_name) -> Optional[str]:
    """
    Send a single prompt to OpenAI and get the response.

    Args:
        prompt (str): The user's input prompt
        model (str): The OpenAI model to use

    Returns:
        Optional[str]: The AI's response or None if there's an error
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1000,
        )

        # Extract the response text
        if response.choices and len(response.choices) > 0:
            return response.choices[0].message.content.strip()
        return None

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
