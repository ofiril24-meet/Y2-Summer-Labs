from flask import Flask

app = Flask( __name__ , template_folder='templates',  static_folder='static'  )
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/')  
def signup():
  return render_template('signup.html')


  @app.route('/signin')  
def signin():
  return render_template('signin.html')


  @app.route('/home')  
def home():
  return render_template('home.html')


  @app.route('/video')  
def video():
  return render_template('video.html')


  @app.route('/stat')  
def stat():
  return render_template('stat.html')


  @app.route('/quiz')  
def quiz():
  return render_template('quiz.html')


  @app.route('/leaderboard')  
def leaderboard():
  return render_template('leaderboard.html')


  if __name__ == "__main__":  
  app.run(debug=True)