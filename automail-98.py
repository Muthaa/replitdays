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
  msg['Subject'] = "Take a BREAK" # Sets the subject of the message
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


# import schedule, time # Import the time library

# def printMe():
#   print("⏰")

# schedule.every(2).seconds.do(printMe)

# while True:
#   schedule.run_pending()
#   time.sleep(1) # Pause for 1 second before moving on