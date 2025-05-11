Graph RAG Examples
==================

This document provides practical examples of using Graph RAG in various scenarios.

Basic Usage
-----------

1. Simple Query
~~~~~~~~~~~~~~~

.. code-block:: python

   from skai.graph_rag import GraphRAG

   # Initialize the client
   rag = GraphRAG(api_key="your-api-key")

   # Simple query
   response = rag.query("What is Graph RAG?")
   print(response.text)

2. Knowledge Graph Creation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Create a knowledge graph
   nodes = [
       {
           "id": "feature1",
           "properties": {
               "name": "Graph Storage",
               "description": "Efficient graph-based data storage"
           }
       },
       {
           "id": "feature2",
           "properties": {
               "name": "Vector Search",
               "description": "Fast similarity search"
           }
       }
   ]

   relationships = [
       {
           "source": "feature1",
           "target": "feature2",
           "type": "COMPLEMENTS"
       }
   ]

   rag.update_graph(nodes=nodes, relationships=relationships)

Advanced Usage
--------------

1. Custom Query Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Query with custom parameters
   response = rag.query(
       query="Explain the architecture",
       max_tokens=2000,
       temperature=0.8,
       top_k=5
   )

2. Batch Processing
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Process multiple queries
   queries = [
       "What are the key features?",
       "How does it work?",
       "What are the benefits?"
   ]

   responses = rag.batch_query(queries)

3. Vector Search
~~~~~~~~~~~~~~~~

.. code-block:: python

   # Perform vector search
   results = rag.vector_search(
       query_vector=[0.1, 0.2, 0.3],
       top_k=3,
       threshold=0.7
   )

Integration Examples
--------------------

1. Flask Web Application
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from flask import Flask, request, jsonify
   from skai.graph_rag import GraphRAG

   app = Flask(__name__)
   rag = GraphRAG(api_key="your-api-key")

   @app.route('/query', methods=['POST'])
   def query():
       data = request.json
       response = rag.query(data['query'])
       return jsonify(response)

   if __name__ == '__main__':
       app.run()

2. FastAPI Integration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from fastapi import FastAPI
   from skai.graph_rag import GraphRAG

   app = FastAPI()
   rag = GraphRAG(api_key="your-api-key")

   @app.post("/query")
   async def query(query: str):
       response = await rag.query_async(query)
       return response

Error Handling
--------------

.. code-block:: python

   try:
       response = rag.query("What is Graph RAG?")
   except Exception as e:
       print(f"Error: {str(e)}")
       # Handle error appropriately 