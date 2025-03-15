# Communication Skills Trainer with LLM

This project is a communication skills trainer that uses language models (like Grok API and Whisper) to provide feedback on user input (both text and voice) for better communication. It offers both text and voice-based interaction with transcription and feedback on communication clarity, tone, and effectiveness.

## Table of Contents

1. [Setup Instructions](#setup-instructions)
2. [Dependencies](#dependencies)
3. [Optimization Choices](#optimization-choices)
4. [Usage Examples](#usage-examples)

## Setup Instructions

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/communication-skills-trainer.git
cd communication-skills-trainer
```

### Step 2: Install Required Dependencies

Install the necessary dependencies using pip:

```bash
pip install -r requirements.txt
```

Ensure that you have Python 3.8+ and pip installed. The dependencies will include:

Gradio for the interface
Whisper for speech-to-text
Grok API for the language model
gTTS for text-to-speech
python-dotenv for loading environment variables

### Step 3: Set Up API Keys

Create a .env file in the root of the project directory.
Add your API key for Grok in the .env file:
```bash
GROQ_API=your_grok_api_key
```
You will also need to download and set up the Whisper model locally or you can use the Hugging Face API.

### Step 4: Run the Application
Once dependencies are installed and your API key is configured, run the application using the following command:

```bash
python main.py
```
This will launch a Gradio interface in your web browser.

### Dependencies
The project requires the following dependencies:

Gradio: For creating the web interface.
Whisper: For transcribing audio to text.
gTTS: For converting text to speech.
Langchain-Grok: To connect to the Grok API for communication feedback.
dotenv: For loading environment variables.

Install all dependencies by running:
```bash
pip install gradio whisper gtts langchain-groq python-dotenv langchain-core ffmpeg langchain
```

Usage Examples
### 1. Text Input Tab
In the "Text Input" tab, users can type their message. The system will process the input and provide feedback on the clarity, tone, and effectiveness of the communication.

Example:

Input: "Hi, I hope you're having a great day!"
Feedback: "The tone is friendly and polite. Consider adding more context to make your message clearer."
### 2. Voice Input Tab
In the "Voice Input" tab, users can either record their voice or upload an audio file. The system will transcribe the audio, process the text, and generate a voice response along with feedback.

Example:

Input (Audio): "Hey, how are you today?"
Transcription: "Hey, how are you today?"
Feedback: "The tone is informal and casual, but it may be too abrupt in formal settings."
### 3. Upload Audio File Tab
Users can upload an audio file directly for transcription. After transcription, the system will display the text and provide feedback on communication effectiveness.

Example:

Input (Audio File): greeting.wav
Transcription: "Good evening, how are you?"
Feedback: "The greeting is polite and professional. Consider varying the tone to avoid sounding monotone."