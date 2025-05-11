AI Agent Examples
=================

This document provides practical examples of using AI Agent in various scenarios.

Basic Usage
-----------

1. Simple Task Creation
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from skai.agent import AIAgent

   # Initialize the client
   agent = AIAgent(api_key="your-api-key")

   # Create a simple task
   response = agent.create_task(
       task="Analyze customer feedback",
       parameters={
           "priority": "medium",
           "context": {
               "customer_id": "12345"
           }
       }
   )
   print(response.task_id)

2. Task Monitoring
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Monitor task progress
   task_status = agent.get_task_status("task_123")
   print(f"Task status: {task_status.status}")
   print(f"Progress: {task_status.progress}%")

Advanced Usage
--------------

1. Batch Task Processing
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Process multiple tasks
   tasks = [
       {
           "task": "Analyze feedback",
           "parameters": {"priority": "high"}
       },
       {
           "task": "Generate report",
           "parameters": {"format": "pdf"}
       }
   ]

   responses = agent.batch_create_tasks(tasks)

2. Custom Agent Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Configure agent with custom settings
   agent.configure(
       agent_id="agent_123",
       settings={
           "learning_rate": 0.001,
           "memory_size": "10GB",
           "max_concurrent_tasks": 5
       }
   )

Integration Examples
--------------------

1. Web Application Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from flask import Flask, request, jsonify
   from skai.agent import AIAgent

   app = Flask(__name__)
   agent = AIAgent(api_key="your-api-key")

   @app.route('/task', methods=['POST'])
   def create_task():
       data = request.json
       response = agent.create_task(
           task=data['task'],
           parameters=data['parameters']
       )
       return jsonify(response)

   if __name__ == '__main__':
       app.run()

2. Task Automation
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import schedule
   import time
   from skai.agent import AIAgent

   agent = AIAgent(api_key="your-api-key")

   def daily_report():
       agent.create_task(
           task="Generate daily report",
           parameters={
               "report_type": "daily",
               "format": "pdf"
           }
       )

   # Schedule daily report generation
   schedule.every().day.at("00:00").do(daily_report)

   while True:
       schedule.run_pending()
       time.sleep(60)

Error Handling
--------------

.. code-block:: python

   try:
       response = agent.create_task("Analyze data")
   except Exception as e:
       print(f"Error: {str(e)}")
       # Handle error appropriately 