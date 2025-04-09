import tkinter as tk
from tkinter import scrolledtext
import requests
import threading

# URL da API
url = "http://127.0.0.1:1234/v1/chat/completions"

def enviar_mensagem():
    pergunta = entrada_usuario.get()
    if not pergunta.strip():
        return
    entrada_usuario.delete(0, tk.END)

    # mensagem do usuário no chat com ícone
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"👤 Você: {pergunta}\n", "usuario")
    chat_log.config(state=tk.DISABLED)

    # carregamento
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, "⏳ O assistente está digitando...\n", "loading")
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)

    # carregamento para não travar a interface
    threading.Thread(target=processar_resposta, args=(pergunta,)).start()

def processar_resposta(pergunta):
    # enviar a mensagem para a API
    resposta_bot = enviar_para_api(pergunta)

    # remove a linha de carregamento
    chat_log.config(state=tk.NORMAL)
    chat_log.delete("end-2l", "end-1l")

    chat_log.insert(tk.END, f"🤖 ChatBOT: {resposta_bot}\n", "chatbot")
    chat_log.insert(tk.END, "\n")
    chat_log.config(state=tk.DISABLED)

    chat_log.yview(tk.END)

def enviar_para_api(pergunta):
    # requisição (JSON)
    payload = {
        "model": "nous-hermes-2-mistral-7b-dpo",
        "messages": [
            {
                "role": "user",
                "content": pergunta,
            }
        ],
        "max_tokens": 500,
        "top_p": 0.5
    }

    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data["choices"][0]["message"]["content"]
        else:
            return f"Erro ao acessar a API. Código de status: {response.status_code}"

    except Exception as e:
        return f"Ocorreu um erro durante a solicitação: {e}"

# janela principal
janela = tk.Tk()
janela.title("ChatBOT - Santander")
janela.geometry("700x500")
janela.resizable(False, False)
janela.configure(bg="#2d2d2d")

# (log de mensagens)
chat_log = scrolledtext.ScrolledText(janela, wrap=tk.WORD, state=tk.DISABLED, height=20, font=("Arial", 12), bg="#1e1e1e", fg="white")
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# estilização das mensagens
chat_log.tag_configure("usuario", foreground="cyan", font=("Arial", 12, "bold"))
chat_log.tag_configure("chatbot", foreground="lightgreen", font=("Arial", 12, "bold"))
chat_log.tag_configure("loading", foreground="orange", font=("Arial", 12, "italic"))

# entrada para o usuário
entrada_usuario = tk.Entry(janela, font=("Arial", 12), bg="#3d3d3d", fg="white")
entrada_usuario.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)

# enviar mensagem ao pressionar Enter
entrada_usuario.bind("<Return>", lambda event: enviar_mensagem())

botao_enviar = tk.Button(janela, text="Enviar Mensagem", command=enviar_mensagem, font=("Arial", 12), bg="#4d4d4d", fg="white")
botao_enviar.pack(side=tk.RIGHT, pady=5, padx=10)

janela.mainloop()