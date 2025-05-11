AgensGraph Examples
===================

This document provides practical examples of using AgensGraph in various scenarios.

Basic Examples
--------------

1. Creating a Social Network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sql

   -- Create a graph for social network
   CREATE GRAPH social_network;

   -- Create person nodes
   CREATE (john:Person {name: 'John', age: 30, city: 'New York'});
   CREATE (jane:Person {name: 'Jane', age: 28, city: 'Boston'});
   CREATE (bob:Person {name: 'Bob', age: 35, city: 'Chicago'});

   -- Create relationships
   MATCH (john:Person {name: 'John'}), (jane:Person {name: 'Jane'})
   CREATE (john)-[r1:KNOWS {since: 2020}]->(jane);

   MATCH (jane:Person {name: 'Jane'}), (bob:Person {name: 'Bob'})
   CREATE (jane)-[r2:KNOWS {since: 2021}]->(bob);

2. Querying the Social Network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sql

   -- Find all friends of John
   MATCH (john:Person {name: 'John'})-[:KNOWS]->(friend:Person)
   RETURN friend.name, friend.city;

   -- Find mutual friends
   MATCH (john:Person {name: 'John'})-[:KNOWS]->(friend:Person)<-[:KNOWS]-(bob:Person {name: 'Bob'})
   RETURN friend.name;

Advanced Examples
-----------------

1. Path Finding
~~~~~~~~~~~~~~~

.. code-block:: sql

   -- Find shortest path between two people
   MATCH path = shortestPath((john:Person {name: 'John'})-[:KNOWS*]-(bob:Person {name: 'Bob'}))
   RETURN path;

   -- Find all paths with maximum length
   MATCH path = (john:Person {name: 'John'})-[:KNOWS*1..3]-(bob:Person {name: 'Bob'})
   RETURN path;

2. Graph Analytics
~~~~~~~~~~~~~~~~~~

.. code-block:: sql

   -- Calculate degree centrality
   MATCH (p:Person)
   RETURN p.name, size((p)-[:KNOWS]-()) as degree
   ORDER BY degree DESC;

   -- Find communities
   MATCH (p:Person)
   WITH p, size((p)-[:KNOWS]-()) as connections
   WHERE connections > 1
   RETURN p.name, connections;

3. Property Graph Operations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sql

   -- Update node properties
   MATCH (p:Person {name: 'John'})
   SET p.age = 31, p.city = 'Los Angeles';

   -- Add relationship properties
   MATCH (john:Person {name: 'John'})-[r:KNOWS]->(jane:Person {name: 'Jane'})
   SET r.last_meet = '2024-01-15';

Integration Examples
--------------------

1. Python with psycopg2
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import psycopg2

   # Connect to AgensGraph
   conn = psycopg2.connect(
       dbname="agens",
       user="postgres",
       password="password",
       host="localhost"
   )

   # Create a cursor
   cur = conn.cursor()

   # Execute a query
   cur.execute("""
       MATCH (p:Person)
       RETURN p.name, p.age
   """)

   # Fetch results
   results = cur.fetchall()
   for row in results:
       print(row)

2. Java with JDBC
~~~~~~~~~~~~~~~~~

.. code-block:: java

   import java.sql.*;

   public class AgensGraphExample {
       public static void main(String[] args) {
           try {
               // Connect to AgensGraph
               Connection conn = DriverManager.getConnection(
                   "jdbc:postgresql://localhost:5432/agens",
                   "postgres",
                   "password"
               );

               // Create a statement
               Statement stmt = conn.createStatement();

               // Execute a query
               ResultSet rs = stmt.executeQuery(
                   "MATCH (p:Person) RETURN p.name, p.age"
               );

               // Process results
               while (rs.next()) {
                   System.out.println(
                       rs.getString("p.name") + ", " +
                       rs.getInt("p.age")
                   );
               }
           } catch (SQLException e) {
               e.printStackTrace();
           }
       }
   }

Performance Optimization
------------------------

1. Index Usage
~~~~~~~~~~~~~~

.. code-block:: sql

   -- Create indexes for frequently queried properties
   CREATE INDEX ON :Person(name);
   CREATE INDEX ON :Person(city);

   -- Use indexes in queries
   MATCH (p:Person {name: 'John'})
   RETURN p;

2. Query Optimization
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: sql

   -- Use LIMIT for large result sets
   MATCH (p:Person)
   RETURN p
   LIMIT 1000;

   -- Use WHERE clauses early
   MATCH (p:Person)
   WHERE p.age > 30
   RETURN p; 