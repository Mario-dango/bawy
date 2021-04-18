import pyttsx3                          #pip install pyttsx3
import datetime
import speech_recognition as sr         #pip install speeechrecognition
import wikipedia                        #pip install wikipedia                                        

voz = pyttsx3.init()

def hablar(audio):
    voz.say(audio)
    voz.runAndWait()
#hablar()

def tiempo():
    tiempo = datetime.datetime.now().strftime("%H:%M:%S")
    hablar("La hora en estos momentos es ")
    hablar(tiempo)
#tiempo()

def dia():
    dia = datetime.datetime.now().date
    anio = datetime.datetime.now().year
    mes = datetime.datetime.now().month

    hablar("El día de hoy es")
    hablar(dia)
    hablar(mes)
    hablar(anio)
#dia()

def saludo():
    hablar("Bienvenido de nuevo! aquí Bawy lo saluda con un abrazo virtual !")
    hablar("iniciando sistemas....")
    tiempo()
    dia()
    hora = datetime.datetime.now().hour  
    if hora>=6 and hora<12:
        hablar("Buenos días señor")
    if hora>=12 and hora<18:
        hablar("Buenas tardes señor")
    #elif hora >= 18 and hora <24:
    else:
        hablar("Buenas noches señor")

    hablar("DangoProtype a su servicio")
#saludo()

def TomarComando():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=5)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5)

        #r.adjust_for_ambient_noise(source, duration=5)
    try:
        print("Reconociendo.....")
        query = r.recognize_google(audio, language='es-AR')
        print(query)
    except Exception as e:
        print(e)
        print("Digalo nuevamente, porfavor")
        hablar("Digalo nuevamente, porfavor")
        return "None"
    return query
TomarComando()

#f __name__ == "__main__":
#
#   saludo()
#
#   while True:
#           query = TomarComando().lower()
#
#           #todos los comandos serán guardados por bajocaso
#           #para un fácil reconocimiento 
#
#           if "time" in query:
#               tiempo()
#
#           elif "día" in query:
#               dia()
#
#           elif "wikipedia" in query:
#               hablar("Buscando en wikipedia...")
#               query = query.replace("wikipedia","")
#               result = wikipedia.summary(query,sentences=3)
#               hablar("Según wikipedia")
#               print(result)
#               
#
#

