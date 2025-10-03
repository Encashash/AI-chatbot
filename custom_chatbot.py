import google.generativeai as genai
import gradio as gr

genai.configure(api_key="AIzaSyA6z75Qa8s_IZLFDx8CL1su-Ws8kAwMQvI")
messages = [{"role": "system", "content": "You are a helpful assistant"}]

def customchatgpt(user_input):
    messages.append({"role": "user", "content": user_input})
    model = genai.GenerativeModel("gemini-2.5-flash")
    message = [msg["content"] for msg in messages]
    response = model.generate_content(message)
    chatgpt_reply = response.text
    messages.append({"role": "assistant", "content": chatgpt_reply})   
    return chatgpt_reply

input_box = gr.Textbox(lines=6, max_lines=10, label="Input")
output_box = gr.Textbox(lines=10, max_lines=20, label="Output")
demo = gr.Interface(fn=customchatgpt, inputs=input_box, outputs=output_box, title="custom chatgpt")
demo.launch(share=True)