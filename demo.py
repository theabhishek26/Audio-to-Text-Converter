import assemblyai as aai
from dotenv import load_dotenv
import os
load_dotenv()

AAI_API_KEY = os.getenv("AAI_API_KEY")


aai.settings.api_key = AAI_API_KEY

# audio_file = "./local_file.mp3"
audio_file = open("static/demo1.mp3","rb")

config = aai.TranscriptionConfig(speech_model=aai.SpeechModel.best)

transcript = aai.Transcriber(config=config).transcribe(audio_file)

if transcript.status == "error":
  raise RuntimeError(f"Transcription failed: {transcript.error}")

print(transcript.text)