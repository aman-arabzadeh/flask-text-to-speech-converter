# app.py
# Text-to-Speech Web App using Flask and gTTS
# Date: 2024-10-04
# Author: Aman Arabzadeh

from flask import Flask, render_template, request
from gtts import gTTS
import os,  uuid
from gtts.lang import tts_langs
app = Flask(__name__)   
# Get available languages from gTTS in dictionary format
AVAILABLE_LANGUAGES = tts_langs()

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html', languages=AVAILABLE_LANGUAGES)


# Function to remove previous audio files
def remove_file_if_exists(file_path):
            #Delete previous audio files
        for file in os.listdir(file_path):
            if file.endswith('.mp3'):   
                os.remove(os.path.join(file_path, file))


# Route to handle form submission and generate speech
@app.route('/generate_speech', methods=['POST'])
def generate_speech():
    # Get form data
    input_text = request.form['text']
    selected_language = request.form['language']
    message = ""
    audio_file_path = None

    # Validate input text
    if not input_text.strip():
        return render_template(
            'index.html',
            audio_file = None,
            message = "Please enter some text.",
            languages = AVAILABLE_LANGUAGES
        )

    try:
        # Remove previous audio files
        remove_file_if_exists('static')
        # Generate speech
        text_to_speach_object = gTTS(text=input_text, lang=selected_language)
        unique_filename = f"speech_{uuid.uuid4().hex}.mp3"
        audio_file_path = os.path.join('static', unique_filename)
        # Save the audio file
        text_to_speach_object.save(audio_file_path)
        message = "Speech generated successfully!"
    except Exception as error:
        message = f"Error generating speech: {error}"
        audio_file_path = None
    # Render the results page
    return render_template(
        'results.html',
        audio_file = unique_filename,
        message = message,
        languages = AVAILABLE_LANGUAGES
    )

# Run the Flask app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

