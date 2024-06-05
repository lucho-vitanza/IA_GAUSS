from flask import request
import requests
from app.transcriber import transcribe_audio
from app.utils import download_audio, save_report

def whatsapp():
    data = request.json
    for entry in data['entry']:
        for message in entry['changes'][0]['value']['messages']:
            if 'audio' in message:
                audio_id = message['audio']['id']
                audio_url = f"https://graph.facebook.com/v12.0/{audio_id}"
                response = requests.get(audio_url, headers={'Authorization': 'Bearer YOUR_ACCESS_TOKEN'})
                audio_path = "path/to/save/audio.ogg"
                with open(audio_path, 'wb') as f:
                    f.write(response.content)
                transcript = transcribe_audio(audio_path)
                save_report(transcript)
                return 'Informe recibido y transcrito'
    return 'No se recibió audio'

