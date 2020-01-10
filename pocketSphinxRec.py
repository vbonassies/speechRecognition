import speech_recognition as sr

r = sr.Recognizer()
harvard = sr.AudioFile('sounds/harvard.wav')
french = sr.AudioFile('sounds/OSR_fr_000_0041_8k.wav')
jack = sr.AudioFile('sounds/jackhammer.wav')

with french as source:
    #r.adjust_for_ambient_noise(source, duration=0.5)
    audio = r.record(source)
    #audio = r.record(source, offset=4, duration=3)

print(r.recognize_sphinx(audio, language='fr-FR'))
