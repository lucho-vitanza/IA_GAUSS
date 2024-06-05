import os

def download_audio(url, token, save_path):
    response = requests.get(url, headers={'Authorization': f'Bearer {token}'})
    with open(save_path, 'wb') as f:
        f.write(response.content)

def save_report(transcript, report_path):
    with open(report_path, 'w') as f:
        f.write(transcript)

