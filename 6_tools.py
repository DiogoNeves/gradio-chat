import gradio as gr
from gradio.external import format_conversation

from model import stream_response


THINKING_MODEL = "deepseek-r1-distill-llama-8b"


def create_message(content: str, title: str | None = None):
    if title is None:
        return gr.ChatMessage(content, role="assistant")
    else:
        return gr.ChatMessage(content, role="assistant", metadata={"title": title})


def generate_conversation(
    prompt: str,
    history: list[gr.MessageDict],
    system_prompt: str,
    temperature: float,
):
    if system_prompt and len(history) == 0:
        history.append(gr.MessageDict(content=system_prompt, role="system"))
    messages = format_conversation(history, prompt)

    turn = []
    for chunk in stream_response(messages, temperature, THINKING_MODEL):
        if chunk == "<think>":
            turn.append(create_message("", "🤔 Thinking..."))
        elif chunk == "</think>":
            turn.append(create_message(""))
        elif not turn:
            turn.append(create_message(chunk))
        else:
            turn[-1].content += chunk
        yield turn


system_prompt = gr.Textbox(
    label="System prompt",
    value="You are a helpful but overthinking and over-opinionated assistant.",
)

temperature = gr.Slider(
    label="Temperature",
    value=0.5,
    minimum=0.0,
    maximum=1.0,
    step=0.01,
)

demo = gr.ChatInterface(
    generate_conversation,
    type="messages",
    autofocus=False,
    additional_inputs=[system_prompt, temperature],
)


if __name__ == "__main__":
    demo.launch()
