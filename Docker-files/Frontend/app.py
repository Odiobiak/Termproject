from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<h1> Python Flask in Docker!</h1>
<p>A sample web-app fo running Flask inside Docker.</p>
"""


# launch the app if the script is involved as the main program
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')