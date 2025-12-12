import gradio as gr

with gr.Blocks() as demo:
    text = gr.Textbox(value=89.0)

    @text.submit(inputs=[], outputs=[])
    def fn_1():
        ...
        return 

demo.launch()