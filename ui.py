# ui.py
import gradio as gr
from main import call_feedback_model, chat_with_voice ,process_audio_file # Import functions from main.py

# Create the UI layout directly
with gr.Blocks() as demo:
    # Tab for Text Input
    with gr.Tab("Text Input"):
        # User input field
        text_input = gr.Textbox(label="Enter Text", placeholder="Type something here...")

        # Chat history output
        chat_output = gr.Textbox(label="Chat History", interactive=False, lines=10)

        # Feedback output
        text_feedback = gr.Textbox(label="Model Feedback", interactive=False)

        # Button to trigger chat
        text_button = gr.Button("Generate Response")

        # Update chat history and feedback after clicking button
        text_button.click(call_feedback_model, inputs=text_input, outputs=[chat_output, text_feedback])

    # Tab for Voice Input
    with gr.Tab("Voice Input"):
        # Audio input from microphone
        audio_input = gr.Audio(sources="microphone", type="filepath", label="Upload/Record Audio")
        text_output_voice = gr.Textbox(label="Transcription", interactive=False)
        text_feedback_voice = gr.Textbox(label="Feedback Response", interactive=False)
        audio_output_voice = gr.Audio(label="Audio Response")
        
        # Button to trigger voice-based interaction
        voice_button = gr.Button("Generate Voice Response")

        # When the button is clicked, trigger the chat_with_voice function
        voice_button.click(chat_with_voice, inputs=audio_input, outputs=[text_output_voice, text_feedback_voice, audio_output_voice])
    
    with gr.Tab("Upload Audio File"):
        file_input = gr.File(label="Upload Audio File")
        file_transcription_output = gr.Textbox(label="Transcription", lines=15, interactive=False)
        file_feedback_output = gr.Textbox(label="Model Feedback", lines=15, interactive=False)
        
        # When file is uploaded, get transcription and feedback
        file_input.change(process_audio_file, inputs=file_input, outputs=[file_transcription_output, file_feedback_output])

# Launch the interface
if __name__ == "__main__":
    demo.launch(share=True)
