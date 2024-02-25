import os, requests, json, openai
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup

import requests
from bs4 import BeautifulSoup

url = "https://lu.ma/replitevents"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

myLinks = soup.find_all("a", {"class":"css-1m051bw"})

max= 10
openai.organisation = os.environ['organisationID']
openai.api_key = os.environ['openai']
openai.Model.list()


print(len(myLinks))

responses = []

counter = 0
for link in myLinks:
  print(link.text)
  if counter > max:
    break
  prompt = (f"""Summarise {link["url"]} in no more than four words.""")
  response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=50)
  #print(response["choices"][0]["text"].strip())
  responses.append(response["choices"][0]["text"].strip())


import schedule, time, os, smtplib # Import the smtp library
from email.mime.multipart import MIMEMultipart # Import the mime library to create multipart messages
from email.mime.text import MIMEText # Import the mime library to create text messages

password = os.environ['mailPassword']
username = os.environ['mailUsername']

def sendMail():
  email = "Don't forget to take a break!" # Contents of the message
  server = "smtp.gmail.com" # Address of the mail server, change it to yours if you need to
  port = 587 # Port of the mail server, change it to yours if you need to
  s = smtplib.SMTP(host = server, port = port) # Creates the server connection using the host and port details
  s.starttls() # Sets the encryption mode
  s.login(username, password) # Logs into the email server for us

  msg = MIMEMultipart() # Creates the message
  msg['To'] = "recipient@email.com" # Sets the receiver's email address
  msg['From'] = username # Sets the sender's email address
  msg['Subject'] = responses # Sets the subject of the message
  msg.attach(MIMEText(email, 'html')) # Attaches the email content to the message as html

  s.send_message(msg) # Sends the message
  del msg # Deletes the message from memory

sendMail() # Call the subroutine to test it.

def printMe():
  print("⏰")

schedule.every(1).hour.do(printMe)

while True:
  schedule.run_pending()
  time.sleep(1)

