import os
import webbrowser
import speech_recognition as sr
import pyttsx3

def svr():


    services = ['Netflix','netflix','Disney+','disney+','Disney','disney','Disney +','disney +', 'Hbo Max', 'hbo Max', 'HboMax', 'hbomax', 'Hbomax', 'Hbomax','hbo','Hbo', 'Prime video', 'prime video', 'Prime', 'prime', 'Amazon Prime','amazon prime',' Crunchyroll', 'crunchyroll']
    urln = 'https://www.netflix.com'
    urld = 'https://www.disneyplus.com'
    urlp = 'https://www.primevideo.com'
    urlh = 'https://play.hbomax.com'
    urlc = 'https://www.crunchyroll.com'
    urlg = 'https://globoplay.globo.com/'
    urlf = 'https://www.funimation.com'
    urla = 'https://tv.apple.com'
    urlst = 'https://www.starplus.com'
    urlyt = 'https://www.youtube.com'
    urls = [ urld, urln, urlp, urlh, urlc, urlg, urlf, urla]
    
    engine = pyttsx3.init()
    r = sr.Recognizer()
    m = sr.Microphone()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say('What Streaming service do you want to watch?')        
    engine.runAndWait()
    
    with m as source:
        engine = pyttsx3.init()
        r = sr.Recognizer()
        m = sr.Microphone()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)        
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        value = r.recognize_google(audio, language='en-US')
        print(value)
        pass
        if value == 'quit':
                quit = True
                engine.say('Welcome back to the main menu')
                engine.runAndWait()
        elif "Netflix" in value : 
                engine.say('Opening the desired streaming service.')
                webbrowser.open(urln)
                engine.runAndWait()    
        elif "Disney Plus" in value:
                engine.say('Opening the desired streaming service.')
                webbrowser.open(urld)
                engine.runAndWait()           
        elif "Amazon prime" "prime" "prime video" in value:
                engine.say('Opening the desired streaming service.')
                webbrowser.open(urlp)
                engine.runAndWait()
        elif "Hbo max" in value:
                engine.say('Opening the desired streaming service.')
                webbrowser.open(urlh)
                engine.runAndWait()
        elif "crunchyroll" in value:
                engine.say('Opening the desired streaming service.')
                webbrowser.open(urlc)
                engine.runAndWait()
        elif "globo play" in value:
                engine.say('Opening the desired streaming service.')
                webbrowser.open(urlg)
                engine.runAndWait()
        elif "funimation" in value:
                engine.say('Opening the desired streaming service.')
                webbrowser.open(urlf)
                engine.runAndWait()
        elif "apple tv" in value:
                engine.say('Opening the desired streaming service.')
                webbrowser.open(urla)
                engine.runAndWait()
        elif "star +" "star+" 'star' in value:
                engine.say('Opening the desired streaming service.')
                engine.runAndWait()
                webbrowser.open(urlst)
        elif "Youtube" in value:
                engine.say('Opening the desired streaming service.')
                engine.runAndWait()
                webbrowser.open(urlyt)
        engine.runAndWait()
svr()