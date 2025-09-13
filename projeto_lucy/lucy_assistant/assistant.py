
import speech_recognition as sr
import pyttsx3
import os
import subprocess
import webbrowser
import sys
from datetime import datetime
import unicodedata

# Inicializa engine de voz
engine = pyttsx3.init()

def speak(text):
    """Fala o texto passado como argumento"""
    print(f"Lucy: {text}")
    engine.stop()  # limpa qualquer fala pendente
    engine.say(text)
    engine.runAndWait()

def listen_command():
    """Escuta o comando de voz do usuário e retorna em texto"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando comando...", end="\r")
        r.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=6)
        except sr.WaitTimeoutError:
            return None

    try:
        comando = r.recognize_google(audio, language="pt-BR").lower()
        print(f"DEBUG: reconhecido -> {comando}")
        return comando
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        speak("Erro ao se conectar ao serviço de reconhecimento.")
        return None

def normalize_text(text):
    """Remove acentos e coloca tudo em minúsculo"""
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    ).lower()

def execute_command(comando):
    """Executa ações de acordo com o comando"""
    comando = normalize_text(comando)

    if "abrir bloco de notas" in comando:
        speak("Abrindo bloco de notas")
        subprocess.Popen(["notepad.exe"])
        return

    elif "abrir calculadora" in comando:
        speak("Abrindo calculadora")
        subprocess.Popen(["calc.exe"])
        return

    elif "abrir navegador" in comando:
        speak("Abrindo navegador")
        webbrowser.open("https://www.google.com")
        return
    
    elif "estudos" in comando:
        speak("Abrindo Udemy para você")
        chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        url = "https://www.udemy.com/"
        try:
            subprocess.Popen([chrome_path, url])
        except FileNotFoundError:
            print("Chrome não encontrado, abrindo no navegador padrão...")
            webbrowser.open(url)
        return

    elif "abrir editor" in comando:
        speak("Abrindo Visual Studio Code")
        try:
            subprocess.Popen(["code"], shell=True)
        except FileNotFoundError:
            speak("Não consegui abrir o VS Code. Verifique se está instalado.")
        return

    elif "que horas sao" in comando or "data" in comando:
        agora = datetime.now()
        speak(f"Agora são {agora.strftime('%H:%M')} do dia {agora.strftime('%d/%m/%Y')}")
        return

    elif "tocar musica" in comando:
        speak("Abrindo Spotify para você")
        try:
            subprocess.Popen(["start", "spotify:"], shell=True)
        except FileNotFoundError:
            speak("Spotify não encontrado.")
        return

    elif "abrir pasta de downloads" in comando:
        pasta_downloads = os.path.expanduser("~/Downloads")
        if os.path.exists(pasta_downloads):
            speak("Abrindo pasta de downloads")
            os.startfile(pasta_downloads)
        else:
            speak("Não encontrei a pasta de downloads.")
        return

    elif comando in ["desligar", "fechar", "sair"]:
        speak("Encerrando o sistema. Até logo!")
        sys.exit()

    else:
        speak("Comando não reconhecido")

def start_lucy():
    """Inicia a Lucy com saudação e loop de comandos"""
    speak("Olá! Estou pronta para ajudar você!")
    while True:
        comando = listen_command()
        if comando:
            execute_command(comando)

if __name__ == "__main__":
    start_lucy()