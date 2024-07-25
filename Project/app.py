from flask import Flask, render_template, url_for, redirect, request
from flask import session  
import pyrebase 

Config = {
  "apiKey": "AIzaSyCcXxSS2HYZXXQjN9anI0EE105uEibdeIo",
  "authDomain": "individual-project-messi.firebaseapp.com",
  "projectId": "individual-project-messi",
  "storageBucket": "individual-project-messi.appspot.com",
  "messagingSenderId": "320663239730",
  "appId": "1:320663239730:web:3c795a51a11833f7dfd02b",
  "measurementId": "G-1XBW3SK1V0", "databaseURL": "https://individual-project-messi-default-rtdb.europe-west1.firebasedatabase.app/"
}

app = Flask( __name__ , template_folder='templates',  static_folder='static'  )
app.config['SECRET_KEY'] = 'super-secret-key'
firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db =firebase.database()


#questions = {"How many Ballon D'ors Has Messi Won?":"Eight"}


@app.route('/', methods=['GET' , 'POST'])  
def signup():
	if request.method == "POST":
		email = request.form['email']
		password = request.form['password']
		username = request.form['username']
		user = {"password":password, "username":username, "email":email}
		
		try:
			session['user'] = auth.create_user_with_email_and_password(email, password)
			UID = session['user']['localId']
			db.child("Users").child(UID).set(user)
			return redirect(url_for('signin'))

		except:
			error = "Authentication failed"
			print(auth.create_user_with_email_and_password(email, password))
			return render_template("signup.html")
	return render_template("signup.html")



@app.route('/signin' , methods=['GET' ,'POST'])  
def signin():
	if request.method == "POST":
		email = request.form['email']
		password = request.form['password']

		try: 
			session['user'] = auth.sign_in_with_email_and_password(email, password)
			return redirect(url_for('home'))
		except:
			error = "authentication error"
			print(error)
			redirect('/error') 
	else:		   
		return render_template("signin.html")
	return render_template('signin.html')


@app.route('/home', methods=['GET' , 'POST'])  
def home():
  return render_template('home.html')


@app.route('/quiz', methods=['GET' , 'POST'])  
def quiz():
	question= db.child("quizes").get().val()
	if request.method == "POST":
		score = 0
		right_answers = db.child("quizes").get().val()
		if request.form["q1"] == right_answers["How many Ballon D'ors Has Messi Won?"]:
			score+=1
		if request.form["q2"] == right_answers["How Many Teams has Messi Played for?"]:	
			score+=1
		if request.form["q3"] == right_answers["What Club Does Messi Play For?"]:	
			score+=1
		if request.form["q4"] == right_answers["What's Messi's Height?"]:
			score+=1	
		if request.form["q5"] == right_answers["Whats's Messi's strong foot"]:	
			score+=1
		print(score)
		

		username=db.child("Users").child(session['user']['localId']).get().val()['username']
		db.child("leaderboard").push({"username": username, "score": score})
		return render_template('leaderboard.html',score=score , username=username)
	return render_template("quiz.html" , question=question)

@app.route('/leaderboard', methods=['GET' , 'POST'])  
def leaderboard():
	print(username)
	print(score)
	return render_template('leaderboard.html')


@app.route('/signout', methods=['GET' , 'POST'])  
def signout():
	if request.method == "GET":
		session.pop('user', None)
		return redirect(url_for('signin'))
	return render_template("signin.html")


@app.route('/video', methods=['GET' , 'POST'])  
def video():
	return render_template("video.html")


if __name__ == "__main__":  
  app.run(debug=True)








  #@app.route('/video', methods=['GET' , 'POST'])  
# def video():
#   return render_template('video.html')


# @app.route('/stat', methods=['GET' , 'POST'])  
# def stat():
#   return render_template('stat.html')