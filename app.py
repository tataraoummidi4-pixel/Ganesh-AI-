import gradio as gr
import os
def ganesh_chat(m,h):
    return f"Jai Ganesh! You said: {m} 🙏 Ganpati Bappa Morya!"
with gr.Blocks(title="Ganesh AI") as demo:
    gr.Markdown("# 🙏 Ganesh AI")
    chatbot=gr.Chatbot(height=400)
    msg=gr.Textbox(label="Message",placeholder="Jai Ganesh!")
    clear=gr.Button("Clear")
    def um(message,history):
        return "",history+[[message,None]]
    def br(history):
        history[-1][1]=ganesh_chat(history[-1][0],history)
        return history
    msg.submit(um,[msg,chatbot],[msg,chatbot]).then(br,chatbot,chatbot)
    clear.click(lambda:None,None,chatbot,queue=False)
if __name__=="__main__":
    port=int(os.environ.get("PORT",10000))
    demo.launch(server_name="0.0.0.0",server_port=port)
