import sys
import threading
# Package make UI
import tkinter


# Speech to text package
import speech_recognition
# Text to speech
import pyttsx3

# Model AI chatbot
from neuralintents import BasicAssistant

class Assistant:
    def __init__(self):
        # Speech recognizer
        self.recognizer = speech_recognition.Recognizer()
        # Voice response instant
        self.speaker = pyttsx3.init()
        self.speaker.setProperty("rate", 150)

        # intent_methods: dictionary to map a tag to a function
        self.assistant = BasicAssistant("intents.json", method_mappings={"file": self.create_file})
        self.assistant.fit_model()

        # Create UI
        self.root = tkinter.Tk()
        self.label = tkinter.Label(self.root, text="Voice Assistant", font=("Arial", 120, "bold"))
        self.label.pack()

        # Create a thread to handle assistant
        threading.Thread(target=self.run_assistant).start()
        # Run UI on main thread
        self.root.mainloop()

    def create_file(self,):
        with open("somefile.txt", "w") as f:
            f.write("Hello World!")

    # Listen for audio and convert it to text
    def run_assistant(self):
        while (True):
            try:
                # Use Microphone resource to listen
                with speech_recognition.Microphone() as mic:
                    # Tự điều chỉnh độ ồn của mic
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    # Get audio from mic
                    audio = self.recognizer.listen(mic)
                    # Convert audio to text
                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()

                    # Cmd khởi động
                    if "hey river" in text:
                        self.label.config(fg="red")
                        # Lắng nghe cmd chính
                        audio = self.recognizer.listen(mic)
                        text = self.recognizer.recognize_google(audio)
                        text = text.lower()
                        print(text)

                        if text == "stop":
                            self.speaker.say("Bye")
                            self.speaker.runAndWait()
                            self.speaker.stop()
                            self.root.destroy()
                            sys.exit(0)
                        else:
                            if text is not None:
                                response = self.assistant.process_input(text)
                                if response is not None:
                                    self.speaker.say(response)
                                    self.speaker.runAndWait()

                            self.label.config(fg="black")
            except speech_recognition.UnknownValueError:
                self.label.config(fg="black")
                continue

def main():
    assistant = Assistant()

if __name__ == "__main__":
    main()