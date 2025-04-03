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
    resposta_bot = f"Olá! 🐾💙 Bem-vindo ao PetCare – seu companheiro virtual para monitorar sua saúde mental enquanto interage com adoráveis pets! 🎓🐶🐱Aqui, você pode acompanhar seu bem-estar emocional, receber dicas para aliviar o estresse acadêmico e, claro, se divertir com interações terapêuticas com nossos amigos peludos.Estamos aqui para tornar sua jornada mais leve e acolhedora. Sempre que precisar, é só chamar! ✨🐾 "

    return jsonify({"resposta": resposta_bot})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
