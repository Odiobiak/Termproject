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
storage_client = storage.Client(project="termproject-273720")

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
        
        #hugo file is submitted
        if request.form.get('Hugo.tar.gz') == 'Hugo.tar.gz':
            #Creating a job client
            job1 = {
                'reference' : {
                    'job_id' : 'jobhugo'
                },
                'placement' : {
                    'cluster_name' : 'cluster-2',
                    #'clusterUuid' : '3d4db54c-3b47-4724-ae02-90b4b825d6df'
                },
                'hadoop_job' : {
                    'main_class' : 'InvertedIndex',
                    'args' : ['gs://dataproc-staging-us-west1-494286768598-sn2scqkt/Data/Hugo.tar.gz', 'gs://dataproc-staging-us-west1-494286768598-sn2scqkt/hugo_out'],
                    'jar_file_uris' : ['gs://dataproc-staging-us-west1-494286768598-sn2scqkt/JAR/invertedindex.jar']
                }
            }
            job_response = job_client.submit_job(project_id, region, job1)
            blob = buckets.get_blob('finalhugo.txt')
            result = blob.download_as_string()
            with open("hugofile.txt", "wb") as fl:
                fl.write(result)
            with open('hugofile.txt', 'r') as f:
                #lines = f.readline().splitlines()
                content = f.readlines()
            return render_template('hugo.html', content=content)

        elif request.form.get('shakespeare.tar.gz') == 'shakespeare.tar.gz':
                  #Creating a job client
            job2 = {
                'reference' : {
                    'job_id' : 'jobshakes'
                },
                'placement' : {
                    'cluster_name' : 'cluster-2',
                    #'clusterUuid' : '3d4db54c-3b47-4724-ae02-90b4b825d6df'
                },
                'hadoop_job' : {
                    'main_class' : 'InvertedIndex',
                    'args' : ['gs://dataproc-staging-us-west1-494286768598-sn2scqkt/Data/shakespeare.tar.gz', 'gs://dataproc-staging-us-west1-494286768598-sn2scqkt/shakespeare_out'],
                    'jar_file_uris' : ['gs://dataproc-staging-us-west1-494286768598-sn2scqkt/JAR/invertedindex.jar']
                }
            }
            job_response2 = job_client.submit_job(project_id, region, job2)
            with open("shakespearfile.txt", "wb") as f1:
                f1.write(result2)
            with open('shakespearfile.txt', 'r') as f1:
                #lines = f.readline().splitlines()
                content = f1.readlines()
            return render_template('shakes.html', content=content)

        elif request.form.get('Tolstoy.tar.gz') == 'Tolstoy.tar.gz':
                  #Creating a job client
            job3 = {
                'reference' : {
                    'job_id' : 'jobtol'
                },
                'placement' : {
                    'cluster_name' : 'cluster-2',
                    #'clusterUuid' : '3d4db54c-3b47-4724-ae02-90b4b825d6df'
                },
                'hadoop_job' : {
                    'main_class' : 'InvertedIndex',
                    'args' : ['gs://dataproc-staging-us-west1-494286768598-sn2scqkt/Data/tolstoy.tar.gz', 'gs://dataproc-staging-us-west1-494286768598-sn2scqkt/tolstoy_out'],
                    'jar_file_uris' : ['gs://dataproc-staging-us-west1-494286768598-sn2scqkt/JAR/invertedindex.jar']
                }
            }
            job_response3 = job_client.submit_job(project_id, region, job3)
            with open("Tolstoyfile.txt", "wb") as f2:
                f2.write(result3)
            with open('Tolstoyfile.txt', 'r') as f2:
                #lines = f.readline().splitlines()
                content = f2.readlines()
            return render_template('Tol.html', content=content)

        elif request.form.get('all') == 'all':
                  #Creating a job client
            job4 = {
                'reference' : {
                    'job_id' : 'joball'
                },
                'placement' : {
                    'cluster_name' : 'cluster-2',
                    #'clusterUuid' : '3d4db54c-3b47-4724-ae02-90b4b825d6df'
                },
                'hadoop_job' : {
                    'main_class' : 'InvertedIndex',
                    'args' : ['gs://dataproc-staging-us-west1-494286768598-sn2scqkt/Data', 'gs://dataproc-staging-us-west1-494286768598-sn2scqkt/all_out'],
                    'jar_file_uris' : ['gs://dataproc-staging-us-west1-494286768598-sn2scqkt/JAR/invertedindex.jar']
                }
            }
            job_response4 = job_client.submit_job(project_id, region, job4)
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
