from flask import Flask, render_template, request, redirect, url_for
import random	

app = Flask(__name__, template_folder = "templates")

@app.route('/', methods=["GET", "POST"])
def login():
	if request.method == 'GET':
		return render_template("login.html")
	else:
		user_name = request.form['username']
		print(login_session)
		birth_month = request.form['birthMonth']
		print(login_session)
		return redirect(url_for('home', birth_month=birth_month, user_name=user_name))	

@app.route('/fortune/<birth_month>')
def fortune(birth_month):
	fortunes_list = ["A thrilling opportunity will soon present itself to you","Your creativity will lead you to great success.","An unexpected journey will change your life for the better.", "A wave of prosperity is coming your way." , "Your efforts will be rewarded with success beyond your expectations." , "Joy and laughter will fill your heart in the days ahead." , "Opportunities for growth and fulfillment are on the horizon." , "Be cautious of trusting others too easily; betrayal lurks nearby." , "A setback in your plans will test your resilience, but you will emerge stronger." , "Miscommunication may lead to misunderstandings with someone dear to you." , "A temporary financial challenge will require careful budgeting and planning."]
	index=len(birth_month)
	chosen=fortunes_list[9]
	if index<10:
		chosen=fortunes_list[index-1]
	return render_template("fortune.html" , chosen=chosen)

@app.route('/home')
def home():
	return render_template("hello.html")


if __name__ == '__main__':
	app.run(debug=True)