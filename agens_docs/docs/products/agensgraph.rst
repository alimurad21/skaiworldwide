AgensGraph
==========

A multi-model hypergraph DBMS combining relational and graph databases.

Overview
--------

AgensGraph is a powerful multi-model database management system that seamlessly integrates relational and graph database capabilities. It provides a unified platform for managing complex data relationships while maintaining the flexibility of traditional relational databases.

Features
--------

* Multi-model database support (Graph + Relational)
* ACID compliance
* SQL and Cypher query languages
* High performance and scalability
* Advanced indexing capabilities
* Enterprise-grade security

Getting Started
---------------

Installation
~~~~~~~~~~~~

.. code-block:: bash

   # Download and install AgensGraph
   wget https://www.bitnine.net/downloads/agensgraph-latest.tar.gz
   tar xvf agensgraph-latest.tar.gz
   cd agensgraph-*
   ./configure
   make
   make install

Basic Usage
~~~~~~~~~~~

.. code-block:: sql

   -- Connect to AgensGraph
   psql -d agens

   -- Create a graph
   CREATE GRAPH graph_name;

   -- Create nodes and relationships
   CREATE (n:Person {name: 'John'})
   CREATE (m:Person {name: 'Jane'})
   CREATE (n)-[:KNOWS]->(m);

Architecture
------------

AgensGraph consists of the following key components:

1. PostgreSQL Core Engine
2. Graph Storage Engine
3. Query Optimizer
4. Transaction Manager
5. Security Layer

For detailed architecture information, see the :doc:`architecture guide </products/agensgraph_architecture>`.

API Reference
-------------

For detailed API documentation, see the :doc:`API reference </products/agensgraph_api>`.

Examples
--------

See our :doc:`examples </products/agensgraph_examples>` for common use cases and implementation patterns. 