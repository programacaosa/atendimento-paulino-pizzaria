import streamlit as st
import os
import time  # Importar o módulo time para simular um atraso

# Função para ler o conteúdo de um arquivo .txt com base no nome do arquivo
def ler_arquivo_por_palavra_chave(nome_arquivo):
    caminho_arquivo = f"cardapio/{nome_arquivo}.txt"  # Altere o caminho para incluir a pasta
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

# Função para buscar arquivos .txt na pasta cardapio e retornar suas palavras-chave
def obter_palavras_chave(pasta):
    palavras_chave = []
    for arquivo in os.listdir(pasta):
        if arquivo.endswith('.txt'):
            nome_arquivo = arquivo[:-4]  # Remove a extensão .txt do nome do arquivo
            palavras_chave.append(nome_arquivo)

    # Adicione mais palavras-chave manualmente, se necessário
    palavras_chave += ['pizza', 'pizzas', 'bebidas', 'opções de pizza', 'opções de pizzas']  # Adicione outras palavras-chave conforme necessário

    return palavras_chave

# Interface do Streamlit
st.title("Perguntas e Respostas com Arquivos de Texto")
st.markdown("Digite sua pergunta relacionada aos nossos arquivos de texto abaixo:")

# Obtém as palavras-chave da pasta 'cardapio'
palavras_chave = obter_palavras_chave('cardapio')  # Passa o caminho da pasta

# Campo para o usuário digitar a pergunta
pergunta = st.text_input("Digite sua pergunta:")

if st.button("Enviar"):
    if pergunta:
        # Exibe a mensagem "Digitando..." enquanto a resposta está sendo buscada
        with st.spinner("Digitando..."):
            time.sleep(4)  # Simula um atraso para dar a sensação de carregamento
            resposta = buscar_resposta_por_palavra_chave(pergunta, palavras_chave)

        # Exibe a resposta
        st.subheader("Resposta:")
        st.write(resposta)
    else:
        st.warning("Por favor, digite uma pergunta antes de enviar.")
