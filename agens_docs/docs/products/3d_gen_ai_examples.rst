3D Gen AI Examples
==================

This document provides practical examples of using 3D Gen AI in various scenarios.

Basic Usage
-----------

1. Simple Model Generation
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from skai.gen3d import Gen3D

   # Initialize the client
   gen3d = Gen3D(api_key="your-api-key")

   # Generate a simple model
   response = gen3d.generate(
       prompt="A modern office building",
       parameters={
           "style": "contemporary",
           "resolution": "medium"
       }
   )
   print(response.model_url)

2. Model Processing
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Process an existing model
   response = gen3d.process(
       model_id="model_123",
       operations=[
           {
               "type": "optimize",
               "parameters": {
                   "quality": "high",
                   "compression": "lossless"
               }
           },
           {
               "type": "texture",
               "parameters": {
                   "style": "photorealistic"
               }
           }
       ]
   )

Advanced Usage
--------------

1. Batch Processing
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Process multiple models
   models = [
       {
           "prompt": "Modern house",
           "parameters": {"style": "contemporary"}
       },
       {
           "prompt": "Ancient temple",
           "parameters": {"style": "historical"}
       }
   ]

   responses = gen3d.batch_generate(models)

2. Custom Parameters
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Generate with custom parameters
   response = gen3d.generate(
       prompt="Futuristic city",
       parameters={
           "style": "cyberpunk",
           "resolution": "ultra",
           "format": "glb",
           "texture_quality": "high",
           "polygon_count": "optimized"
       }
   )

Integration Examples
--------------------

1. Unity Integration
~~~~~~~~~~~~~~~~~~~~

.. code-block:: csharp

   using SKAI.Gen3D;

   public class ModelGenerator : MonoBehaviour
   {
       private Gen3DClient client;

       void Start()
       {
           client = new Gen3DClient("your-api-key");
       }

       async void GenerateModel()
       {
           var response = await client.GenerateAsync(
               "Futuristic vehicle",
               new GenerationParameters
               {
                   Style = "cyberpunk",
                   Resolution = "high"
               }
           );

           // Load the model in Unity
           await LoadModel(response.ModelUrl);
       }
   }

2. Blender Integration
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import bpy
   from skai.gen3d import Gen3D

   def generate_and_import():
       # Initialize client
       client = Gen3D(api_key="your-api-key")

       # Generate model
       response = client.generate(
           prompt="Organic sculpture",
           parameters={"style": "abstract"}
       )

       # Import into Blender
       bpy.ops.import_scene.gltf(filepath=response.model_path)

Error Handling
--------------

.. code-block:: python

   try:
       response = gen3d.generate("Modern building")
   except Exception as e:
       print(f"Error: {str(e)}")
       # Handle error appropriately 