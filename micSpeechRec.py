import speech_recognition as sr

r = sr.Recognizer()
#print(sr.Microphone.list_microphone_names())
mic = sr.Microphone()
response = {
    "success": True,
    "error": None,
    "transcription": None
}

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

try:
    rec = r.recognize_google(audio, language="fr-FR")
    response["transcription"] = rec
    print(rec)

except sr.RequestError:
    # API was unreachable or unresponsive
    response["success"] = False
    response["error"] = "API unavailable"
except sr.UnknownValueError:
    # Speech was unintelligible
    response["error"] = "Unable to recognize speech"

print(response)
