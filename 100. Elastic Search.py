# Python code snippet that demonstrates how to connect to an Elasticsearch instance, index data, and perform a search query:

from elasticsearch import Elasticsearch

# create an Elasticsearch instance
es = Elasticsearch(['http://localhost:9200/'])

# create an index with mappings
index_name = 'my_index'
index_mappings = {
    'mappings': {
        'properties': {
            'title': {'type': 'text'},
            'description': {'type': 'text'},
            'price': {'type': 'float'}
        }
    }
}
es.indices.create(index=index_name, body=index_mappings)

# add documents to the index
doc1 = {
    'title': 'Product 1',
    'description': 'This is the first product',
    'price': 10.99
}
doc2 = {
    'title': 'Product 2',
    'description': 'This is the second product',
    'price': 19.99
}
es.index(index=index_name, body=doc1)
es.index(index=index_name, body=doc2)

# perform a search query
search_query = {
    'query': {
        'match': {
            'description': 'product'
        }
    }
}
search_results = es.search(index=index_name, body=search_query)

# print the search results
for hit in search_results['hits']['hits']:
    print(hit['_source']['title'], hit['_source']['description'], hit['_source']['price'])

# This code creates an Elasticsearch instance, creates an index with mappings, indexes two documents, and performs a search query for documents that contain the term "product" in the description field. The search results are then printed to the console. Note that you will need to install the elasticsearch Python module before running this code.
