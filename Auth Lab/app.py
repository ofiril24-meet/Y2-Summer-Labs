from flask import Flask, render_template, url_for, redirect, request
from flask import session  
import pyrebase 
Config = {
  "apiKey": "AIzaSyD_Az6MhQvqbCEgK-9IvRmRwJ0vzl3RHss",
  "authDomain": "auth-lab-8688a.firebaseapp.com",
  "projectId": "auth-lab-8688a",
  "storageBucket": "auth-lab-8688a.appspot.com",
  "messagingSenderId": "978452626136",
  "appId": "1:978452626136:web:d00bd1793b2f5c805275ad",
  "measurementId": "G-58YG8M907C", "databaseURL":"https://auth-lab-8688a-default-rtdb.europe-west1.firebasedatabase.app/"
  }
app = Flask( __name__ , template_folder='templates',  static_folder='static'  )
app.config['SECRET_KEY'] = 'super-secret-key'
firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()
db =firebase.database()


@app.route("/", methods=['GET' , 'POST'])  
def signup():
  if request.method == "POST":
    email = request.form['email']
    password = request.form['password']
    full_name = request.form['full_name']
    username = request.form['username']
    session['quotes'] = []
    user = {"full_name":full_name, "username":username, "email":email}
    UID = session['user']['localId']
    db.child("Users").child(UID).update(updated)


    try:
      session['user'] = auth.create_user_with_email_and_password(email, password)
      session['quote'] = quuote
      return redirect(url_for('signin'))
    except:
      error = "Authentication failed"
      print(auth.create_user_with_email_and_password(email, password))
      return render_template("signup.html")
  return render_template("signup.html")
  


@app.route('/home', methods=['GET' , 'POST'])  
def home():
  if request.method == "POST":
    quote = request.form['quote']
    quote_dict = {"text": quote ,"said_by":who_qoute, "UID":"session['user']['localId']" }
    # session['quotes'].append(quote)
    # session.modified = True
    return redirect(url_for('thanks'))
  return render_template('home.html')

 
@app.route('/signin' , methods=['GET' ,'POST'])  
def signin():
  if request.method == "POST":
    # return render_template('signin.html')
    email = request.form['email']
    password = request.form['password']
    
    try: 
      session['user'] = auth.sign_in_with_email_and_password(email, password)

      return redirect(url_for('home'))
    except:
      error = "authentication error"
      print(error)
      redirect('/error')
  return render_template("signin.html")
  


@app.route('/display')  
def display():
  return render_template('display.html')


@app.route('/thanks')  
def thanks():
  return render_template('thanks.html')

@app.route('/signout')  
def signout():
  session.pop('user', None)
  session.pop('qoutes', None)
  return redirect(url_for('signin'))

  

if __name__ == "__main__":  
  app.run(debug=True)
