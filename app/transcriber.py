from faster_whisper import WhisperModel

def transcribe_audio(audio_path):
    model = WhisperModel("large-v2")
    segments, info = model.transcribe(audio_path)
    
    transcript = ""
    for segment in segments:
        transcript += segment.text
    
    return transcript

