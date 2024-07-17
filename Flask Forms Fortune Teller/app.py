from flask import Flask, render_template
import random

app = Flask(__name__, template_folder = "templates")

@app.route('/')
def home():
	return render_template("hello.html")

@app.route('/fortune')
def fortune():
	fortunes_list = ["A thrilling opportunity will soon present itself to you","Your creativity will lead you to great success.","An unexpected journey will change your life for the better.", "A wave of prosperity is coming your way." , "Your efforts will be rewarded with success beyond your expectations." , "Joy and laughter will fill your heart in the days ahead." , "Opportunities for growth and fulfillment are on the horizon." , "Be cautious of trusting others too easily; betrayal lurks nearby." , "A setback in your plans will test your resilience, but you will emerge stronger." , "Miscommunication may lead to misunderstandings with someone dear to you." , "A temporary financial challenge will require careful budgeting and planning."


]
	rnd_fortune = random.randint(1,3)
	chosen = fortunes_list[rnd_fortune]
	return render_template("fortune.html", chosen=chosen)



if __name__ == '__main__':
	app.run(debug=True)