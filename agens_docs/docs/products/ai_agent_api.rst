AI Agent API Reference
======================

This document provides detailed information about the AI Agent API endpoints and usage.

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

1. Task Management
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   POST /api/v1/tasks

   {
       "task": "Analyze customer feedback",
       "parameters": {
           "priority": "high",
           "deadline": "2024-03-20",
           "context": {
               "customer_id": "12345",
               "feedback_type": "product_review"
           }
       }
   }

2. Agent Control
~~~~~~~~~~~~~~~~

.. code-block:: python

   POST /api/v1/agents/control

   {
       "agent_id": "agent_123",
       "action": "pause",
       "parameters": {
           "reason": "maintenance",
           "duration": "1h"
       }
   }

3. Knowledge Base
~~~~~~~~~~~~~~~~~

.. code-block:: python

   POST /api/v1/knowledge/query

   {
       "query": "What are the best practices for customer service?",
       "context": {
           "domain": "customer_service",
           "language": "en"
       }
   }

Python SDK
----------

The AI Agent Python SDK provides a convenient interface to the API:

.. code-block:: python

   from skai.agent import AIAgent

   # Initialize client
   agent = AIAgent(api_key="YOUR_API_KEY")

   # Create a task
   response = agent.create_task(
       task="Analyze customer feedback",
       parameters={
           "priority": "high",
           "context": {
               "customer_id": "12345"
           }
       }
   )

   # Control agent
   agent.control(
       agent_id="agent_123",
       action="pause",
       parameters={
           "reason": "maintenance"
       }
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