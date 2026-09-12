import gradio as gr
from transformers import pipeline

# Simple chat brain - will work on free CPU
chat = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")

def ganesh_chat(message):
    prompt = f"You are Ganesh AI, helpful assistant for 9th class. Answer simply: {message}"
    ans = chat(prompt, max_new_tokens=200)[0]['generated_text']
    return ans

def ganesh_image(prompt):
    # For permanent app, we block personal real photos for safety
    blocked = ["real person", "my friend", "my girlfriend", "girl photo", "boy photo"]
    if any(w in prompt.lower() for w in blocked):
        return "Ganesh AI only creates new art - like logos, festival backgrounds, study diagrams, cartoon avatars. Please don't use names of real people."

    # For now we show text, later you can connect Stable Diffusion
    return f"Image prompt received: '{prompt}' - Connect SDXL model when you get GPU access"

with gr.Blocks(title="Ganesh AI") as app:
    gr.Markdown("# 🤖 Ganesh AI - Permanent Version")
    gr.Markdown("Made by Ganesh - Answers all questions + Creates images")

    with gr.Tab("Chat"):
        q = gr.Textbox(label="Ask anything")
        a = gr.Textbox(label="Answer")
        btn = gr.Button("Ask")
        btn.click(ganesh_chat, q, a)

    with gr.Tab("Create Image"):
        p = gr.Textbox(label="Image prompt", placeholder="Ex: Diwali background, cartoon elephant logo")
        out = gr.Textbox(label="Output")
        btn2 = gr.Button("Generate")
        btn2.click(ganesh_image, p, out)

app.launch()