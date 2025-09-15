# Lucy_assistant
# 🤖 Lucy Assistente

Lucy é um **assistente virtual por voz**, desenvolvido em **Python**, que executa comandos no seu computador de forma prática e interativa.  
Com ela, você pode abrir programas, acessar sites, consultar a hora e até ouvir música — tudo por comando de voz!

---

## ✨ Funcionalidades

- 🎙 **Reconhecimento de voz** (usando `speech_recognition`)
- 🔊 **Resposta falada** (usando `pyttsx3`)
- 📝 Abrir programas do Windows (Bloco de Notas, Calculadora, VS Code)
- 🌐 Abrir navegador e sites (Google, Udemy)
- 🎶 Abrir o Spotify
- ⏰ Informar hora e data atuais
- 📂 Abrir pasta de downloads
- ❌ Encerrar o sistema por comando de voz

---

## 🛠 Tecnologias Usadas

- [Python 3](https://www.python.org/)
- [speech_recognition](https://pypi.org/project/SpeechRecognition/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [webbrowser](https://docs.python.org/3/library/webbrowser.html)
- [subprocess](https://docs.python.org/3/library/subprocess.html)

---

## 🚀 Como Usar

1. **Clone o repositório**
   ```bash
   git clone https://github.com/bertollimb/lucy-assistente.git
   cd lucy-assistente

2. **Instale as dependências**
pip install speechrecognition pyttsx3

3. **Execute o projeto**
python lucy.py

4. **Fale um dos comandos suportados, por exemplo:**

- "abrir bloco de notas"

- "abrir navegador"

- "que horas são"

- "tocar música"

- "desligar"

**📌 Observações**

O projeto foi desenvolvido para Windows. Alguns comandos podem não funcionar em outros sistemas operacionais.

É necessário ter um microfone configurado para usar o reconhecimento de voz.

Para abrir o Visual Studio Code, é preciso que o comando code esteja configurado no PATH do sistema.


