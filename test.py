import pyttsx3
import datetime
import speech_recognition as sr

voz = pyttsx3.init()

def hablar(audio):
    voz.say(audio)
    voz.runAndWait()

def time_():
    tiempo = datetime.datetime.now().strftime("%H:%M:%S")
    hablar("La hora en estos momentos es ")
    hablar(tiempo)

time_()

def inicio():
     hora = datetime.datetime.now().hour

    if hora>=6 and hora<12:
        hablar("Buenos días señor")
    elif hora>=12 and hora<18:
        hablar("Buenas tardes señor")
    #elif hora >= 18 and hora <24:
    else:
        hablar("Buenas noches señor")

    hablar("DangoProtype a su servicio")

def TomarComando():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Reconociendo.....")
        query = r.recognize_google(audio, language='es')
        print(query)

    except Exception as e:
        print(e)
        print("Digalo nuevamente, porfavor")
        hablar("Digalo nuevamente, porfavor")
        return "None"

    return query

TomarComando()
