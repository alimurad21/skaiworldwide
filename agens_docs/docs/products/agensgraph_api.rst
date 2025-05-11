AgensGraph API Reference
========================

This document provides detailed information about the AgensGraph API and its usage.

SQL API
-------

1. Graph Creation
~~~~~~~~~~~~~~~~~

.. code-block:: sql

   -- Create a new graph
   CREATE GRAPH graph_name;

   -- Create a graph with options
   CREATE GRAPH graph_name
   WITH (
       max_nodes = 1000000,
       max_edges = 5000000
   );

2. Node Operations
~~~~~~~~~~~~~~~~~~

.. code-block:: sql

   -- Create a node
   CREATE (n:Person {name: 'John', age: 30});

   -- Create multiple nodes
   CREATE (n:Person {name: 'John'}), (m:Person {name: 'Jane'});

   -- Match and update nodes
   MATCH (n:Person {name: 'John'})
   SET n.age = 31;

3. Relationship Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sql

   -- Create a relationship
   MATCH (a:Person), (b:Person)
   WHERE a.name = 'John' AND b.name = 'Jane'
   CREATE (a)-[r:KNOWS]->(b);

   -- Create relationship with properties
   CREATE (a)-[r:KNOWS {since: 2020}]->(b);

4. Graph Queries
~~~~~~~~~~~~~~~~

.. code-block:: sql

   -- Find all friends of friends
   MATCH (a:Person)-[:KNOWS]->(b:Person)-[:KNOWS]->(c:Person)
   WHERE a.name = 'John'
   RETURN c.name;

   -- Path finding
   MATCH path = shortestPath((a:Person)-[:KNOWS*]-(b:Person))
   WHERE a.name = 'John' AND b.name = 'Jane'
   RETURN path;

Cypher API
----------

1. Basic Queries
~~~~~~~~~~~~~~~~

.. code-block:: cypher

   // Find all nodes
   MATCH (n) RETURN n;

   // Find nodes with label
   MATCH (n:Person) RETURN n;

   // Find nodes with property
   MATCH (n:Person {name: 'John'}) RETURN n;

2. Pattern Matching
~~~~~~~~~~~~~~~~~~~

.. code-block:: cypher

   // Find relationships
   MATCH (a:Person)-[r:KNOWS]->(b:Person)
   RETURN a, r, b;

   // Variable length paths
   MATCH (a:Person)-[:KNOWS*1..3]->(b:Person)
   RETURN a, b;

3. Aggregation
~~~~~~~~~~~~~~

.. code-block:: cypher

   // Count nodes
   MATCH (n:Person)
   RETURN count(n);

   // Group by property
   MATCH (n:Person)
   RETURN n.city, count(n);

Administrative API
------------------

1. Graph Management
~~~~~~~~~~~~~~~~~~~

.. code-block:: sql

   -- List all graphs
   SELECT * FROM agens_graph.graphs;

   -- Drop a graph
   DROP GRAPH graph_name;

2. Index Management
~~~~~~~~~~~~~~~~~~~

.. code-block:: sql

   -- Create an index
   CREATE INDEX ON :Person(name);

   -- List indexes
   CALL db.indexes();

3. Statistics
~~~~~~~~~~~~~

.. code-block:: sql

   -- Get graph statistics
   CALL db.stats();

   -- Get node statistics
   CALL db.stats.nodes();

Error Handling
--------------

Common error codes and their meanings:

* 22000: Data exception
* 23000: Integrity constraint violation
* 42000: Syntax error
* 42601: Invalid syntax
* 42703: Undefined column
* 42804: Datatype mismatch

Performance Tuning
------------------

* Index usage guidelines
* Query optimization tips
* Memory configuration
* Cache management 