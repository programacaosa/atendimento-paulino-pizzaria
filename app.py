import streamlit as st
import os
import time
from datetime import datetime  # Importa a biblioteca datetime para obter a hora atual

# Função para ler o conteúdo de um arquivo .txt com base no nome do arquivo
def ler_arquivo_por_palavra_chave(nome_arquivo):
    caminho_arquivo = f"cardapio/{nome_arquivo}.txt"  # Altera o caminho para incluir a pasta
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'r', encoding='utf-8') as file:
            return file.read()  # Retorna o conteúdo do arquivo
    else:
        return None  # Retorna None se o arquivo não existir

# Função para buscar a palavra-chave (nome do arquivo) na pergunta do usuário
def buscar_resposta_por_palavra_chave(pergunta, palavras_chave):
    for chave in palavras_chave:
        if chave in pergunta.lower():  # Verifica se a palavra-chave está na pergunta
            resposta = ler_arquivo_por_palavra_chave(chave)  # Lê o conteúdo do arquivo correspondente
            if resposta:
                return resposta  # Retorna o conteúdo do arquivo se encontrado
            else:
                return "Desculpe, não encontrei o arquivo correspondente."  # Exibe apenas essa mensagem se o arquivo não existir
    return "Desculpe, não encontrei uma resposta adequada para a sua pergunta."

# Função para identificar saudações e responder
def verificar_saudacao(pergunta):
    hora_atual = datetime.now().hour
    if "bom dia" in pergunta.lower():
        return "Bom dia! Como posso ajudar você hoje?"
    elif "boa tarde" in pergunta.lower():
        return "Boa tarde! Como posso ajudar você hoje?"
    elif "boa noite" in pergunta.lower():
        return "Boa noite! Como posso ajudar você hoje?"
    else:
        # Verifica a hora atual para dar uma resposta padrão
        if hora_atual < 12:
            return "Bom dia! Como posso ajudar você hoje?"
        elif 12 <= hora_atual < 18:
            return "Boa tarde! Como posso ajudar você hoje?"
        else:
            return "Boa noite! Como posso ajudar você hoje?"

# Função para buscar arquivos .txt na pasta e retornar suas palavras-chave
def obter_palavras_chave(pastas):
    palavras_chave = []
    for pasta in pastas:
        for arquivo in os.listdir(pasta):
            if arquivo.endswith('.txt'):
                nome_arquivo = arquivo[:-4]  # Remove a extensão .txt do nome do arquivo
                palavras_chave.append(nome_arquivo)

    # Adicione mais palavras-chave manualmente, se necessário
    palavras_chave += ['pizza', 'pizzas', 'bebidas', 'opções de pizza', 'opções de pizzas', 'alho', 'alcaparras', 'alcachofra', 'funcionamento']  # Adicionando 'funcionamento'

    return palavras_chave

# Interface do Streamlit
st.title("Perguntas e Respostas com Arquivos de Texto")
st.markdown("Digite seu nome e sua pergunta relacionada aos nossos arquivos de texto abaixo:")

# Obtém as palavras-chave das pastas 'cardapio' e 'info'
pastas = ['cardapio', 'info']  # Lista de pastas
palavras_chave = obter_palavras_chave(pastas)  # Passa o caminho das pastas

# Campo para o usuário digitar o nome
nome_usuario = st.text_input("Digite seu nome:")

# Campo para o usuário digitar a pergunta
pergunta = st.text_input("Digite sua pergunta:")

if st.button("Enviar"):
    if nome_usuario.strip() and pergunta.strip():  # Verifica se o nome e a pergunta não estão vazios
        # Primeiro, verifica se a pergunta contém uma saudação
        saudacao_resposta = verificar_saudacao(pergunta)
        if "Bom" in saudacao_resposta:  # Se for uma saudação, responda com ela
            resposta = f"{saudacao_resposta} {nome_usuario}!"
        else:
            # Exibe a mensagem "Digitando..." enquanto a resposta está sendo buscada
            with st.spinner("Digitando..."):
                time.sleep(4)  # Simula um atraso para dar a sensação de carregamento
                resposta = buscar_resposta_por_palavra_chave(pergunta, palavras_chave)

        # Formata a resposta com o nome do cliente
        resposta_formatada = f"Então {nome_usuario}: {resposta}"

        # Exibe a resposta
        st.subheader("Resposta:")
        st.write(resposta_formatada)
    else:
        st.warning("Por favor, digite seu nome e uma pergunta antes de enviar.")
