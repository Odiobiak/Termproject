# Odiche Obiakarije
from flask import Flask
from flask import render_template, url_for, redirect, request
import argparse
import time
from os import environ
from google.cloud import dataproc_v1
from google.cloud import storage

app = Flask(__name__)

'''Storage Client'''
storage_client = storage.Client.from_service_account_json(
    'termproject-273720-0d7405cf24f6.json')

#job_client
job_client = dataproc_v1.JobControllerClient(client_options={
    'api_endpoint': 'us-west1-dataproc.googleapis.com:443'
})

#cluster client
cluster_client = dataproc_v1.ClusterControllerClient(client_options={
    'api_endpoint': 'us-west1-dataproc.googleapis.com:443'
})

# TODO: Initialize `project_id`:
project_id = 'termproject-273720'

# TODO: Initialize `region`:
region = 'us-west1'

# Cluster name
cluster_name = 'cluster-2'

cluster_info = cluster_client.get_cluster(project_id, region, cluster_name)
#geting bucket
buckets = storage_client.get_bucket(cluster_info.config.config_bucket)
blob2 = buckets.get_blob('finalsharespeare.txt')
result2 = blob2.download_as_string()

blob3 = buckets.get_blob('finaltolstoy.txt')
result3 = blob3.download_as_string()

blob4 = buckets.get_blob('finalall.txt')
result4 = blob4.download_as_string()


'''Home Route'''
@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    # print(downloaded_blob)
    #content = ''
    if request.method == 'POST':
        #result = request.form
        if request.form.get('Hugo.tar.gz') == 'Hugo.tar.gz':
            blob = buckets.get_blob('finalhugo.txt')
            result = blob.download_as_string()
            with open("hugofile.txt", "wb") as fl:
                fl.write(result)
            with open('hugofile.txt', 'r') as f:
                #lines = f.readline().splitlines()
                content = f.readlines()
                #for line in content:
                    #content = content.splitlines()
                    #print (line)
            return render_template('hugo.html', content=content)

        elif request.form.get('shakespeare.tar.gz') == 'shakespeare.tar.gz':
            with open("shakespearfile.txt", "wb") as f1:
                f1.write(result2)
            with open('shakespearfile.txt', 'r') as f1:
                #lines = f.readline().splitlines()
                content = f1.readlines()
            return render_template('shakes.html', content=content)

        elif request.form.get('Tolstoy.tar.gz') == 'Tolstoy.tar.gz':
            with open("Tolstoyfile.txt", "wb") as f2:
                f2.write(result3)
            with open('Tolstoyfile.txt', 'r') as f2:
                #lines = f.readline().splitlines()
                content = f2.readlines()
            return render_template('Tol.html', content=content)

        elif request.form.get('all') == 'all':
            with open("all.txt", "wb") as f3:
                f3.write(result4)
            with open('all.txt', 'r') as f3:
                #lines = f.readline().splitlines()
                content = f3.readlines()
            return render_template('all.html', content=content)
    return render_template('layout.html')

# launch the app if the script is involved as the main program
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
