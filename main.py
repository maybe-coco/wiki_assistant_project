import speech_recognition as sr
import pyttsx3
import wikipedia
import time

def speak(text):
    engine = pyttsx3.init()  # Every time fresh init
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Voice assistant initialized. Ask me anything!")
    while True:
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening....")
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
                question = recognizer.recognize_google(audio)

                # Wikipedia
                try:
                    summary = wikipedia.summary(question, sentences=6)
                    print(summary)

                    combined_text = f"You asked: {question}. Here is the answer. {summary}"
                    speak(combined_text)

                except wikipedia.DisambiguationError:
                    speak("Your question is too broad. Please be more specific.")
                except wikipedia.PageError:
                    speak("Sorry, I could not find anything on that.")
                    
            except sr.WaitTimeoutError:
                continue
            except sr.UnknownValueError:
                continue
            except sr.RequestError:
                continue
