import gradio as gr


gr.load_chat(
    base_url="http://localhost:1234/v1",
    model="llama-3.2-1b-instruct",
    token="***",
    streaming=True,
).launch()
