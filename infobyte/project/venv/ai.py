import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import smtplib
import imaplib
import email
from email.header import decode_header
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import json


          #Voice Assistant Class

class VoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with self.microphone as source:
            audio = self.recognizer.listen(source)
            try:
                return self.recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                return None

    def send_email(self, recipient, subject, body):
        # Replace with your email credentials
        sender_email = "lokhandkarhariom@gmail.com"
        sender_password = "@Devil118"

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        message = f"Subject: {subject}\n\n{body}"
        server.sendmail(sender_email, recipient, message)
        server.quit()

    def set_reminder(self, reminder_time, reminder_message):
        # Replace with your reminder logic
        print(f"Reminder set for {reminder_time}: {reminder_message}")

    def get_weather_update(self, location):
        # Replace with your weather API logic
        print(f"Weather update for {location}: Sunny")

    def control_smart_home_device(self, device_name, action):
        # Replace with your smart home device logic
        print(f"{device_name} {action}")

    def answer_general_knowledge_question(self, question):
        try:
            answer = wikipedia.summary(question, sentences=2)
            return answer
        except wikipedia.exceptions.DisambiguationError as e:
            return str(e)

    def tell_joke(self):
        return pyjokes.get_joke()


        #Main Function

def main():
    assistant = VoiceAssistant()

    while True:
        command = assistant.listen()
        if command is None:
            continue

        command = command.lower()

        if "send email" in command:
            recipient = input("Enter recipient's email: ")
            subject = input("Enter email subject: ")
            body = input("Enter email body: ")
            assistant.send_email(recipient, subject, body)
        elif "set reminder" in command:
            reminder_time = input("Enter reminder time: ")
            reminder_message = input("Enter reminder message: ")
            assistant.set_reminder(reminder_time, reminder_message)
        elif "weather update" in command:
            location = input("Enter location: ")
            assistant.get_weather_update(location)
        elif "control smart home device" in command:
            device_name = input("Enter device name: ")
            action = input("Enter action: ")
            assistant.control_smart_home_device(device_name, action)
        elif "answer question" in command:
            question = input("Enter question: ")
            answer = assistant.answer_general_knowledge_question(question)
            print(answer)
        elif "tell joke" in command:
            joke = assistant.tell_joke()
            print(joke)
        elif "exit" in command:
            break
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
