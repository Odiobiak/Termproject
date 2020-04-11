from flask import Flask
from flask import render_template, url_for, redirect, request

app = Flask(__name__)

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # this will return the inverted index file
        result = request.form
    return render_template('layout.html', result=result)


# launch the app if the script is involved as the main program
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')