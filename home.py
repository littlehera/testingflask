from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
	return "HOME PAGE GOES HERE"

if __name__ == "__main__":
	app.run()
