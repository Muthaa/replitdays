from flask import Flask , request, redirect

app = Flask(__name__)

@app.route('/')
def index():
	# return redirect('/login')
	# @ login
  	# if user == admin 
  	# 	redirect to admin page 
  	# else if user == user 
  	# 	redirect to home app

  return redirect('/theme')
  
@app.route('/theme',methods=['GET','POST'])
def theme():
  
  return 'thmee'
  

app.run(host='0.0.0.0', port = 81)
