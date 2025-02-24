import gradio as gr
import openai


client = openai.OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="***",
)


def generate_conversation(message, history):
    response = client.chat.completions.create(
        model="llama-3.2-1b-instruct",
        messages=[{"role": "user", "content": message}],
    )
    return response.choices[0].message.content


demo = gr.ChatInterface(
    generate_conversation,
    type="messages",
)


if __name__ == "__main__":
    demo.launch()
