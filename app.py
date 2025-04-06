from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)  # Para permitir requisições do frontend

# Rota principal, que carrega a página do chat
@app.route('/')
def index():
    return render_template('app.html', time=time.time())

@app.route('/chat')
def chatbot():
    return render_template('chatbot.html', time=time.time())

@app.route("/enviar_mensagem", methods=["POST"])
def responder():
    dados = request.get_json()
    mensagem_usuario = dados.get("message", "")

    # Lógica de resposta do bot (aqui um exemplo simples)
    resposta_bot = f"Olá! Seja bem-vindo(a) ao PetMind! 🐶💬 Estamos aqui para ajudar você a cuidar da sua saúde mental de um jeito leve e afetuoso — com a ajuda do seu pet! 🐾✨ O PetMind foi criado especialmente para estudantes como você, que enfrentam uma rotina intensa e, muitas vezes, estressante. Vamos juntos nessa? 💙"

    return jsonify({"resposta": resposta_bot})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
