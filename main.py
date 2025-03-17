# main.py
import os
import gradio as gr
from gtts import gTTS
import whisper
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import re

# Set up environment variables
load_dotenv()
api_key = os.environ.get('GROQ_API')

# Load Whisper model for speech-to-text
whisper_model = whisper.load_model("base")

# Define a PromptTemplate for communication feedback
prompt_template = PromptTemplate(
    input_variables=["input_text"],
    template="You are a communication expert. Provide feedback on the clarity, tone, and effectiveness of the following message:\n{input_text}"
)

# Global chat history
chat_history = []

# Load Grok model
grok = ChatGroq(
    model="llama3-8b-8192",
    #model="mixtral-8x7b-32768",
    temperature=0.8,
    groq_api_key = api_key
    # other params...
)

# Function to call the Grok model API
def call_grok_api(user_input):

    # Use the StrOutputParser to parse the response as a string
    output_parser = StrOutputParser()
    chain = prompt_template | grok | output_parser
    parsed_response = chain.invoke({'input_text': str(user_input)})
    return parsed_response

# Function to transcribe audio to text using Whisper
def transcribe_audio(audio_file):
    if audio_file is None:
        return "No audio file provided."
    
    try:
        # Transcribe audio using Whisper model
        result = whisper_model.transcribe(audio_file, fp16=False)
        return result["text"]
    except Exception as e:
        # Handle any errors during transcription
        return f"Error during transcription: {str(e)}"

# Function to convert text to speech using gTTS
def text_to_speech(text):
    # Ensure the input is a string
    if hasattr(text, 'content'):
        response_text = text.content  # Extract content from an AIMessage object
    else:
        response_text = str(text)  # Convert other types to string

    tts = gTTS(response_text, lang='en')
    audio_path = "response.mp3"
    tts.save(audio_path)
    return audio_path

# Gradio function for text-based input
def call_feedback_model(user_input):
    """Handles user text input, gets response, and stores chat history."""
    """Handles user input and generates feedback on clarity, tone, and effectiveness."""
    global chat_history

    # Get feedback from Grok model based on user input
    feedback = call_grok_api(user_input)  # This calls Grok API to get feedback

    # Store the feedback in the chat history for displaying
    chat_history.append(f"User: {user_input}\nFeedback: {feedback}")

    # Display the last 5 messages (conversation history)
    chat_history_display = "\n\n".join(chat_history[-5:])

    return chat_history_display, feedback 

def clean_text(response):
    """Removes special characters and converts fractions like '2/5' to '2 out of 5'."""
    # Remove '**' around text manually
    clean_response = response.replace('**', '')  # This removes any '**' marks
    clean_response = clean_response.replace('*', '') # This removes any '*' marks
    # Regex to find any fraction in the form of 'X/Y' and convert it to 'X out of Y'
    clean_response = re.sub(r'(\d+)/(\d+)', r'\1 out of \2', clean_response)

    return clean_response


# Gradio function for voice input
def chat_with_voice(audio_file):
    transcription = transcribe_audio(audio_file)
    response = call_grok_api(transcription)
    # removed special char
    clean_response = clean_text(response)
    audio_path = text_to_speech(clean_response)
    return transcription, clean_response, audio_path

# main.py

# processing audio file input, transcription, and feedback
def process_audio_file(audio_file):
    transcription = transcribe_audio(audio_file)  # Transcribe the audio to text
    if transcription:
        # Call the Grok API for feedback based on the transcription
        feedback = call_grok_api(transcription)
        return transcription, feedback
    else:
        return "Error in transcription", "No feedback available"
