3D Gen AI API Reference
=======================

This document provides detailed information about the 3D Gen AI API endpoints and usage.

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

1. Model Generation
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   POST /api/v1/generate

   {
       "prompt": "A futuristic cityscape",
       "parameters": {
           "style": "cyberpunk",
           "resolution": "high",
           "format": "glb"
       }
   }

2. Model Processing
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   POST /api/v1/process

   {
       "model_id": "model_123",
       "operations": [
           {
               "type": "optimize",
               "parameters": {
                   "quality": "high",
                   "compression": "lossless"
               }
           }
       ]
   }

3. Asset Management
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   GET /api/v1/assets

   {
       "filter": {
           "type": "model",
           "status": "completed"
       },
       "page": 1,
       "limit": 10
   }

Python SDK
----------

The 3D Gen AI Python SDK provides a convenient interface to the API:

.. code-block:: python

   from skai.gen3d import Gen3D

   # Initialize client
   client = Gen3D(api_key="YOUR_API_KEY")

   # Generate a model
   response = client.generate(
       prompt="A futuristic cityscape",
       parameters={
           "style": "cyberpunk",
           "resolution": "high"
       }
   )

   # Process a model
   client.process(
       model_id="model_123",
       operations=[{
           "type": "optimize",
           "parameters": {
               "quality": "high"
           }
       }]
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