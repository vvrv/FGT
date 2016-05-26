from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/hello/<name>")
def hello(name):
	return "Hei, " + name + "!"
 
@app.route("/run")
def run():
	lotto = ""
	for i in range(1,7):
		lotto += str(random.randint(0,32)) + ", "
	lotto += str(random.randint(0,32))
	return lotto

if __name__ == "__main__":
    app.run()