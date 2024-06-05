from flask import Flask
from app.whatsapp_bot import whatsapp

app = Flask(__name__)

@app.route('/whatsapp', methods=['POST'])
def handle_whatsapp():
    return whatsapp()

if __name__ == '__main__':
    app.run(debug=True)

