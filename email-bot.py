import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()
def get_info():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass
def send_email(reciver,subject,message):
    server =smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('Digitransolutions2021@gmail.com','Vikas@2021')
    email =EmailMessage()
    email['From'] ='Digitransolutions2021@gmail.com'
    email['To'] =reciver
    email['subject']= subject
    email.set_content(message)
    server.send_message(email)
email_list={
        'vikas':'vikaskncse20@gmail.com',
        'ravish':'raveeshcse20@gmail.com',
        'samarth':'byatnalsamarth@gmail.com',
        'ravi':'raveesh0319@gmail.com',
        'tanish':'rtanish791@gmail.com'
}


def get_email_info():
    talk('To Whom you want to send email')
    name=get_info()
    reciver = email_list[name]
    print(reciver)
    talk('What is the subject of your email?')
    subject=get_info()
    talk('Tell me the text in your email')
    message=get_info()
    send_email(reciver, subject, message)

get_email_info()