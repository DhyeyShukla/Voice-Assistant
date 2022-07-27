import speech_recognition as sr
import webbrowser
import pywhatkit as kit
import pyttsx3 as p
import time

r = sr.Recognizer()
engine =p.init()
voices=engine.getProperty("voices")
rate=engine.getProperty('rate')
engine.setProperty('rate',170)
engine.setProperty('voice',voices[1].id)
engine.say("Hello I am your voice assistant,how can i help you")
engine.runAndWait()
def record_audio():
        with sr.Microphone() as source:
             r.energy_threshold=10000
             r.adjust_for_ambient_noise(source,1.2)
             print('listening')
             voice_data=''
             try:
               audio =r.listen(source)
               voice_data = r.recognize_google(audio)
             except sr.UnknownValueError:
                 print("sorry I am not able to get it")
                 engine.say("sorry I am not able to get it")
        return voice_data

def resopnd(voice_data):
    engine.say(voice_data)
    engine.runAndWait()
# if "search" or "youtube" or "wikipedia" or "play"  not  in voice_data.lower():
#      resopnd("sorry i am not able to understand")
#      engine.runAndWait()
def find(voice_data):
    if "search" in voice_data:
         a = voice_data.index("search")
         url = "https://google.com/search?q="+voice_data[a+7:]
         webbrowser.get().open(url)
         exit()
    if "open youtube" in voice_data.lower():
         url = 'https://www.youtube.com/'
         webbrowser.get().open(url)
         exit()

    if "play" and" youtube"  in voice_data.lower():
        a=voice_data.index("play")
        b = voice_data.index("on")
        url = 'https://www.youtube.com/results?search_query=' + voice_data[a + 5:b]
        resopnd('playing' + voice_data[a + 5:b] + 'on youtube')
        kit.playonyt(voice_data[a + 5:b])
        exit()

        # webbrowser.get().open(url)
    if   "wikipedia" in voice_data.lower():
        # a = voice_data.index("search")
        b = voice_data.index("on")
        url="https://en.wikipedia.org/wiki/"+voice_data[0:b]
        resopnd('searching' + voice_data[0:b] + 'on wikipwdia')
        webbrowser.get().open(url)
        exit()
    if "what time is it" in voice_data:
        print(time.ctime())
    if "find location" in voice_data:
        a = voice_data.index("of")

        url = "https://www.google.com/maps/place/" + voice_data[a+3:]
        resopnd('searching location of' + voice_data[a+3:] + 'on google maps')
        webbrowser.get().open(url)
    if "exit" in voice_data.lower():
        exit()
time.sleep(1)
while (1):
     voice_data=record_audio()
     find(voice_data)

    # pyautogui.click(504,596)
    # pyautogui.typewrite(voice_data[a+7:b])
    # pyautogui.typewrite(["enter"])
