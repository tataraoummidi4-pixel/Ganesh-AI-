import gradio as gr
import os

def chat(m, h):
    reply = "Jai Ganesh! You said: " + m
    return reply

with gr.Blocks() as demo:
    gr.Markdown("# Ganesh AI")
    bot = gr.Chatbot()
    txt = gr.Textbox()
    def ask(msg, hist):
        hist = hist + [[msg, chat(msg, hist)]]
        return "", hist
    txt.submit(ask, [txt, bot], [txt, bot])

port = int(os.environ.get("PORT", 10000))
demo.launch(server_name="0.0.0.0", server_port=port)
