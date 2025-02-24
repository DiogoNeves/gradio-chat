import gradio as gr


def generate_response(message, history):
    return gr.ChatMessage("Hello World", role="assistant")


demo = gr.ChatInterface(
    generate_response,
    type="messages",
)


if __name__ == "__main__":
    demo.launch()
