from flask import Flask, request,redirect

app = Flask(__name__)

@app.route('/language', methods = ["GET"])
def lang():
  data = request.args
  if data == {}:
    return "Nothing here"
  if data["lang"]=="eng":
    return "Hello, and welcome to our wonderful website!"
  elif data["lang"]=="wel":
    return "Helo, a chroeso i'n gwefan wych!"
    # usage /language?lang=wel
    
@app.route('/')
def index():
    return redirect('/language')

app.run(host='0.0.0.0', port=81)