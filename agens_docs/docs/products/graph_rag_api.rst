Graph RAG API Reference
=======================

This document provides detailed information about the Graph RAG API endpoints and usage.

Authentication
--------------

All API requests require authentication using an API key:

.. code-block:: python

   headers = {
       'Authorization': 'Bearer YOUR_API_KEY',
       'Content-Type': 'application/json'
   }

Core Endpoints
--------------

1. Query Endpoint
~~~~~~~~~~~~~~~~~

.. code-block:: python

   POST /api/v1/query

   {
       "query": "What are the key features of Graph RAG?",
       "max_tokens": 1000,
       "temperature": 0.7
   }

2. Knowledge Graph Update
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   POST /api/v1/graph/update

   {
       "nodes": [
           {
               "id": "node1",
               "properties": {
                   "name": "Feature A",
                   "description": "Description of feature A"
               }
           }
       ],
       "relationships": [
           {
               "source": "node1",
               "target": "node2",
               "type": "RELATES_TO"
           }
       ]
   }

3. Vector Search
~~~~~~~~~~~~~~~~

.. code-block:: python

   POST /api/v1/vector/search

   {
       "query_vector": [...],
       "top_k": 5,
       "threshold": 0.8
   }

Python SDK
----------

The Graph RAG Python SDK provides a convenient interface to the API:

.. code-block:: python

   from skai.graph_rag import GraphRAG

   # Initialize client
   client = GraphRAG(api_key="YOUR_API_KEY")

   # Query the system
   response = client.query(
       query="What are the key features?",
       max_tokens=1000
   )

   # Update knowledge graph
   client.update_graph(
       nodes=[...],
       relationships=[...]
   )

Error Handling
--------------

Common error codes and their meanings:

* 400: Bad Request
* 401: Unauthorized
* 403: Forbidden
* 404: Not Found
* 429: Too Many Requests
* 500: Internal Server Error

Rate Limits
-----------

* 100 requests per minute for standard tier
* 1000 requests per minute for enterprise tier 