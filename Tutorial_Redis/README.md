# **What is Redis?**

Link Youtube Part 1: [What is Redis?](https://www.youtube.com/watch?v=LNsqFf7Pu4I)

Link Youtube Part 2: [Learn how to Launch Redis on Windows using Docker](https://www.youtube.com/watch?v=YhXeiB_1-uk&list=PL9nWRykSBSFjj3mulDfc6Al4v8ORNKzaM)

Link Youtube Part 3: [Use Redis with NodeJS](https://www.youtube.com/watch?v=u0_w7McIzFE&list=PL9nWRykSBSFjj3mulDfc6Al4v8ORNKzaM&index=3)

## **REDIS PART 1**
**Objectives:**
- What is Reddis?
- Reddis Modules
- Use Cases
- Pros and Cons
-----------------------
### **1. What is Reddis?**
Gained Popularity as a NoSQL Caching Solution, Founded in 2011. In Memory database (different with SQL). More than just key value - Supports Complex Datastructures: List, map, set, sorted set. Provide Command. 
### **2. Reddis Modules**
Modules allow you to add aditional behaviour, RedisSearch, RedisGraph, RedisStream 
### **3. Use Cases**
- Optimization : if you have a problem query a big data from database, and allow you to cache it and retrieve value more faster. 
- Database : Can be a database
- Leaderboard : Sorted
- Message Broker : PubSub, setup topic
- Data Stream Engine 
- TTL (Time to Live) 
### **4. Pros and Cons**
PRO :
- Simple Intuitive
- Fast in milisecond
- Large Community
- Transactions 
- Scalable 
CON :
- Persistence/Recovery : in memory so it can kill you machine and data can be lost
- No Relationships
- No Access Controls
- Scaling can be Tricky

### **Syntax Example**
Strings
```
> set mykey somevalue
OK
> get mykey
"somevalue"
```
Lists
```
> rpush mylist a b c 
(integer) 3
> rpop mylist
"c"
> rpop mylist
"b"
> rpop mylist
"a"
```
TTL
```
> set key some-value
OK
> expire key 5
(integer) 1
> get key (immediately)
"some-value"
> get key (after some time)
(nil)
```