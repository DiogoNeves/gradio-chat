import gradio as gr
from gradio import ChatMessage
from model import get_ai_response


def generate_response(history):
    # Get the last user message or use a default
    last_message = "What can you help me with?"
    if history and len(history) > 0:
        last_message = history[-1].content

    # Get AI response
    response = get_ai_response(last_message)

    if response:
        # Add the response to history
        history.append(ChatMessage(role="assistant", content=response))
        yield history
    else:
        # Handle error case
        history.append(
            ChatMessage(
                role="assistant",
                content="I apologize, but I encountered an error generating a response.",
                metadata={"title": "💥 Error"},
            )
        )
        yield history


def like(evt: gr.LikeData):
    print("User liked the response")
    print(evt.index, evt.liked, evt.value)


with gr.Blocks() as demo:
    chatbot = gr.Chatbot(
        type="messages",
        height=500,
        show_copy_button=True,
        show_label=False,
        text_align="left",
    )
    msg = gr.Textbox(
        placeholder="Enter your message here...", container=False, autofocus=True
    )
    with gr.Row():
        submit = gr.Button("Submit")
        clear = gr.Button("Clear")

    # Handle interactions
    submit.click(generate_response, [chatbot], [chatbot], queue=True).then(
        lambda: "", None, [msg], queue=False
    )

    msg.submit(generate_response, [chatbot], [chatbot], queue=True).then(
        lambda: "", None, [msg], queue=False
    )

    clear.click(lambda: None, None, chatbot, queue=False)
    chatbot.like(like)

if __name__ == "__main__":
    demo.launch()
