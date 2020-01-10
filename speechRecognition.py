import speech_recognition as sr

r = sr.Recognizer()
harvard = sr.AudioFile('sounds/harvard.wav')
french = sr.AudioFile('sounds/OSR_fr_000_0041_8k.wav')
jack = sr.AudioFile('sounds/jackhammer.wav')

response = {
    "success": True,
    "error": None,
    "transcription": None
}

with harvard as source:
    # r.adjust_for_ambient_noise(source, duration=0.5)
    audio = r.record(source, duration=4)
    audio2 = r.record(source, duration=3)
    # audio = r.record(source, offset=4, duration=3)

try:
    print("----------------------------------------------------------------")
    rec = r.recognize_google(audio)
    print("google audio1: " + rec)
    response["transcription"] = rec
    print("sphinx audio1 (offline): " + r.recognize_sphinx(audio))
    print("----------------------------------------------------------------")
    rec = r.recognize_google(audio2)
    print("google audio2: " + rec)
    response["transcription"] += ", " + rec
    print("sphinx audio2 (offline): " + r.recognize_sphinx(audio2))
    print("----------------------------------------------------------------")
    # print(r.recognize_google(audio, language='fr-FR'))

except sr.RequestError:
    # API was unreachable or unresponsive
    response["success"] = False
    response["error"] = "API unavailable"
except sr.UnknownValueError:
    # Speech was unintelligible
    response["error"] = "Unable to recognize speech"

print(response)