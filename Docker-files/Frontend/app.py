from flask import Flask
from flask import render_template, url_for, redirect, request
import argparse

from google.cloud import dataproc_v1
from google.cloud import storage

app = Flask(__name__)


# Explicitly use service account credentials by specifying the private key
# file.

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    storage_client = storage.Client.from_service_account_json(
'termproject-273720-0d7405cf24f6.json')
    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    #print(buckets)
    result =''
    if request.method == 'POST':
        # this will return the inverted index file
        result = request.form
    return render_template('layout.html', result=result, buckets=buckets)


# launch the app if the script is involved as the main program
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')