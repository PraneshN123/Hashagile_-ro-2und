from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200, 'scheme': 'http'}])

# Check if the connection is successful
if es.ping():
    print("Connected to Elasticsearch!")
else:
    print("Connection failed!")