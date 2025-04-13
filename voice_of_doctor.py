import os
from gtts import gTTS
import elevenlabs 
from  elevenlabs.client import ElevenLabs
import subprocess
import platform
# Use Model for output to voice
def text_to_speech_with_gtts(input_text, output_filepath):
    language = "en"

    audioobj = gTTS(text=input_text, lang=language, slow=False)
    audioobj.save(output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":
            subprocess.run(['powershell', '-c' , f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":
            subprocess.run(['aplay', output_filepath])
        else:
            raise OSError("Unsupported Operating System")
    except Exception as e:
        print("An error has occured while trying to play the audio")

input_text = "Hello, how can I assist you today? new Version"
text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts.mp3")

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_elevenlabs(input_text , output_filepath):
    client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text=input_text,
        voice="Jessica",
        output_format="mp3_22050_32",
        model="eleven_multilingual_v2",
    )
    elevenlabs.save(audio, output_filepath)
    os_name = platform.system()
    try:
        if os_name == "Darwin":  # macOS
            subprocess.run(['afplay', output_filepath])
        elif os_name == "Windows":
            subprocess.run(['powershell', '-c' , f'(New-Object Media.SoundPlayer "{output_filepath}").PlaySync();'])
        elif os_name == "Linux":
            subprocess.run(['aplay', output_filepath])
        else:
            raise OSError("Unsupported Operating System")
    except Exception as e:
        print("An error has occured while trying to play the audio")
text_to_speech_with_elevenlabs(input_text , output_filepath="elevenlabs.mp3")

# def text_to_speech_with_gtts_old(input_text, output_filepath):
#     language = "en"

#     audioobj = gTTS(text=input_text, lang=language, slow=False)
#     audioobj.save(output_filepath)

# input_text = "Hello, how can I assist you today?"
# #text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

# ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

# def text_to_speech_with_elevenlabs_old(input_text , output_filepath):
#     client=ElevenLabs(api_key=ELEVENLABS_API_KEY)
#     audio = client.generate(
#         text=input_text,
#         voice="Jessica",
#         output_format="mp3_22050_32",
#         model="eleven_multilingual_v2",
#     )
#     elevenlabs.save(audio, output_filepath)
#text_to_speech_with_elevenlabs_old(input_text , output_filepath="elevenlabs_testing.mp3")

