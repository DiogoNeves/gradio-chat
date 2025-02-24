import gradio as gr
from gradio.external import format_conversation

from model import stream_response


def generate_conversation(prompt, history):
    messages = format_conversation(history, prompt)
    response = ""
    for chunk in stream_response(messages):
        response += chunk
        yield response


demo = gr.ChatInterface(generate_conversation, type="messages", autofocus=False)


if __name__ == "__main__":
    demo.launch()
