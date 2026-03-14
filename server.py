from flask import Flask, request, send_file
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "API Demucs funcionando!"

@app.route("/separar", methods=["POST"])
def separar():
    file = request.files["audio"]
    path = "input.mp3"
    file.save(path)

    # Separar música usando Demucs
    os.system(f"demucs --two-stems=vocals {path}")

    # Caminho padrão do arquivo gerado
    voz = "separated/htdemucs/input/vocals.wav"
    instrumental = "separated/htdemucs/input/no_vocals.wav"

    return send_file(voz)

app.run(host="0.0.0.0", port=10000)
