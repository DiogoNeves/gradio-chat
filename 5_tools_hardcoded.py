import gradio as gr


def generate_conversation(prompt, history):
    return [
        gr.ChatMessage(
            "Some thinking goes here",
            role="assistant",
            metadata={"title": "Thinking..."},
        ),
        gr.ChatMessage("Hello World", role="assistant"),
    ]


demo = gr.ChatInterface(generate_conversation, type="messages", autofocus=False)


if __name__ == "__main__":
    demo.launch()
