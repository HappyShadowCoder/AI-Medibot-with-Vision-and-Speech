import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path , timeout=20 , phrase_time_limit=None):
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noice...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start Speaking Now...")
            #Record Audio
            audio_data = recognizer.listen(source , timeout=timeout,phrase_time_limit=phrase_time_limit)
            logging.info("Recording Complete.")
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_file(BytesIO(wav_data)) 
            audio_segment.export(file_path, format="mp3" , bitrate="128k")
            logging.info(f"Audio saved to {file_path}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

audio_file_path="patient_voice.mp3"
record_audio(file_path=audio_file_path)

# Speech to Text
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
stt_model="whisper-large-v3"
def transcribe_with_groq(stt_model , audio_filepath,GROQ_API_KEY):
    client = Groq(api_key=GROQ_API_KEY)
    audio_file=open(audio_filepath, "rb")
    transcription = client.audio.transcriptions.create(
    model=stt_model,
    file=audio_file,
    language="en",
    )
    return transcription.text
