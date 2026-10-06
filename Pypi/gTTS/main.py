from gtts import gTTS

texto = "Olá! Este é um teste do Google Text to Speech."

tts = gTTS(text=texto, lang="pt-br")
tts.save("audio.mp3")

print("Áudio criado com sucesso!")
