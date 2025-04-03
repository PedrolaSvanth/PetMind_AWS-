async function enviarMensagem() {
    const input = document.getElementById("user-input");
    const userText = input.value.trim();
    if (!userText) return;

    // Adiciona a mensagem do usuário no chat
    adicionarMensagemNoChat(userText, "usuario");

    // Limpa o campo de input
    input.value = "";

    try {
        const response = await fetch("/enviar_mensagem", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ message: userText }),
        });
        const data = await response.json();

        // Adiciona a resposta do "bot" no chat
        adicionarMensagemNoChat(data.resposta, "bot");
    } catch (error) {
        console.error("Erro ao enviar mensagem:", error);
    }
}

// Função para exibir mensagem no chat
function adicionarMensagemNoChat(texto, tipo) {
    const chatMessages = document.getElementById("chat-messages");
    const mensagem = document.createElement("div");
    mensagem.classList.add("mensagem", tipo);
    mensagem.textContent = texto;
    chatMessages.appendChild(mensagem);

    // Rola para a última mensagem
    chatMessages.scrollTop = chatMessages.scrollHeight;
}