from flask import Flask, render_template, request

app: Flask = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/quiz', methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        return render_template("result.html")
    if request.method == "GET":
        return render_template("quiz.html")
    return render_template("quiz.html")
