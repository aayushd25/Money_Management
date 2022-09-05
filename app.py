from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def root():
    return render_template("index.html")
    
@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/questions")
def questions():
    return render_template("questions.html")


if __name__ == "__main__":
    app.run(debug=True)