import time
from os import environ
# Imports the Google Cloud client library
from google.cloud import storage
from google.cloud import dataproc_v1

storage_client = storage.Client.from_service_account_json(
'termproject-273720-0d7405cf24f6.json')

#buckets = list(storage_client.list_buckets())
#print(buckets)

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

#iterate over the jobs
#for element in cluster_client.list_jobs(project_id,region):
#    print(element)

#Creating a job client
job1 = {
    'reference' : {
        'job_id' : 'j-w'
    },
    'placement' : {
        'cluster_name' : 'cluster-2',
        #'clusterUuid' : '3d4db54c-3b47-4724-ae02-90b4b825d6df'
    },
    'hadoop_job' : {
        'main_class' : 'InvertedIndex',
        'args' : ['gs://dataproc-staging-us-west1-494286768598-sn2scqkt/Data/Hugo.tar.gz', 'gs://dataproc-staging-us-west1-494286768598-sn2scqkt/oip'],
        'jar_file_uris' : ['gs://dataproc-staging-us-west1-494286768598-sn2scqkt/JAR/invertedindex.jar']
    }
}

#job_response = job_client.submit_job(project_id, region, job1)
#job_id = job_response.reference.project_id
#print(job_response)

''' Terminal states for a job.
terminal_states = {
    dataproc_v1.types.JobStatus.ERROR,
    dataproc_v1.types.JobStatus.CANCELLED,
    dataproc_v1.types.JobStatus.DONE
}'''

'''timeout_seconds = 20
time_start = time.time()

# Wait for the job to complete.
while job_response.status.state is 'DONE':
    if time.time() > time_start + timeout_seconds:
        print('Job {} timed out after threshold of {} seconds.'.format(
            job_id, timeout_seconds))
    # Poll for job termination once a second.
    time.sleep(1)
    #job_response = job_client.get_job(project_id, region, job_id)
'''
#getting the output
cluster_info = cluster_client.get_cluster(project_id, region, cluster_name)

#geting bucket
buckets = storage_client.get_bucket(cluster_info.config.config_bucket)
print(buckets)
blob = buckets.get_blob('finalhugo.txt')
downloaded_blob = blob.download_as_string()
print(downloaded_blob)
