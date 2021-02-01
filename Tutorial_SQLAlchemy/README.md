# **SQLite with Python**

Link Tutorial = [SQLite Database with Python - freeCodeCamp.org](https://www.youtube.com/watch?v=byHcYRpMgI4)

### 1. Connect to Database in Python
```python
import sqlite3

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')
```
```
> python try_db.py
```
**Result:** It will create a new file `customer.db`
### 2. Create a Table
*Cursor:* Tell the database anything what you want to do. declare it as `c`
```python
# Create a cursor
c = conn.cursor()

# Create a Table
query = """--sql
CREATE TABLE customers (
        first_name text, 
        last_name text,
        email text)
        
--endsql"""

c.execute(query)

# NULL ==> None
# INTEGER ==> Number
# REAL ==> Decimal
# TEXT ==> Text
# BLOB ==> Imange, mp3, etc

# Commit our command
conn.commit()

# Close our Connection
conn.close()
```
```
> python try_db.py
```
**Result:** Create a new table in SQLite Database as `customers` table

### 3. Insert One Record into Table 
```python
# Insert a Value into Customer Table
query1 = """--sql
INSERT INTO customers 
VALUES ('Merry', 'Brown', 'john3@codemy.com')
--endsql"""

# Execute Query
c.execute(query1)

print('Command Executed Succesfully...')
```
### 4. Insert Many Records into Table
```python
# Insert many customers
many_customers = [('Wes', 'brown', 'Wes@brown.com'),
                 ('Steph', 'Kews', 'steph@kewh.com'),
                 ('Dan', 'Pas', 'dan@pas.com')]

# Execute Many Data
query = """--sql 
INSERT INTO customers 
VALUES (?,?,?)
--endsql"""

c.executemany(query, many_customers)
```

### 5. Query and Fetchall
```python
# Query the Database
query = """--sql 
        SELECT * FROM customers
        --endsql"""

# Execute Query
c.execute(query)

#c.fetchone()
#c.fetchmany(3)
print(c.fetchall())
```
**Results:** [('John', 'Elder', 'john@codemy.com'), ('Tim', 'Elder2', 'john2@codemy.com'), ('Merry', 'Brown', 'john3@codemy.com'), ('Wes', 'brown', 'Wes@brown.com'), ('Steph', 'Kews', 'steph@kewh.com'), ('Dan', 'Pas', 'dan@pas.com')] 

### 6. Format your Results
```python
items = c.fetchall()

print("NAME " + "\t\tEMAIL")
print("_______" + "\t\t" + "_________")
for item in items:
        print(item[0]+" "+item[1]+"\t\t"+item[2])
```
**Return:** 
NAME            EMAIL
John Elder      john@codemy.com
Tim Elder2      john2@codemy.com
Merry Brown     john3@codemy.com
Wes brown       Wes@brown.com
Steph Kews      steph@kewh.com
Dan Pas         dan@pas.com

### 7. Primary Key
```python
# Query the Database
query = """--sql 
        SELECT rowid, * FROM customers
        --endsql"""

# Execute Query
c.execute(query)
```
### 8. Use the Where Clause
```python
# Query the Database
query = """--sql 
        SELECT * FROM customers
        WHERE last_name = 'Elder'
        --endsql"""

# Execute Query
c.execute(query)
```
### 9. Update Records
```python
# Update Records
query = """--sql 
        UPDATE customers 
        SET first_name = 'Bob'
        WHERE last_name = 'Elder'
        --endsql"""

# Execute Query
c.execute(query)
```
### 10. Delete Records
```python
# Delete Records
query = """--sql 
        DELETE FROM customers 
        WHERE rowid = 6
        --endsql"""

# Execute Query
c.execute(query)
```
### 11. Order Results
```python
# Query the Database - Order by
query = """--sql 
        SELECT rowid, * FROM customers
        ORDER BY rowid DESC
        --endsql"""

# Execute Query
c.execute(query)
```
### 12. And/Or
```python
# Query the Database
query = """--sql 
        SELECT rowid, * FROM customers
        WHERE last_name LIKE 'Br%'
        AND rowid = 3
        --endsql"""

# Execute Query
c.execute(query)
```
```python
# Query the Database
query = """--sql 
        SELECT rowid, * FROM customers
        WHERE last_name LIKE 'Br%'
        OR rowid = 3
        --endsql"""

# Execute Query
c.execute(query)
```
### 13. Limiting Results
```python
# Query the Database - Limit
query = """--sql 
        SELECT rowid, * FROM customers
        ORDER BY rowid DSC LIMIT 2 
        --endsql"""

# Execute Query
c.execute(query)
```
### 14. Delete (Drop) A Table and Backups
```python
# Query the Database - Limit
query1 = """--sql 
        DROP TABLE customers
        --endsql"""


# Execute Query
c.execute(query1)
```
### 15. Show All Function
`database.py`
```python
# Query the DB and Return All Records
def show_all():
    # Connect to Database
    conn = sqlite3.connect('custormer.db')

    #Create a cursor 
    c = conn.cursor()

    # Query the Database
    c.execute("""--sql 
    SELECT rowid, * FROM customers
    --endsql""")

    items = c.fetchall()

    for item in items:
        print(item)
    
    # Commit our command 
    conn.commit()

    #Close our connection
    conn.close()
```
`our_app.py`
```python
import database

database.show_all()
```
### 16. Add A Record Function
`database.py`
```python
# Add A New Record to the Table
def add_one(first, last, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("""--sql
    INSERT INTO customers VALUES (?,?,?)
    --endsql""", (first, last, email))

    # Commit our command 
    conn.commit()

    #Close our connection
    conn.close()
```
`our_app.py`
```python
import database

database.add_one("Laura","Smith",'Laura@smith.com')
```
### 17. Delete a Record Function
`database.py`
```python
# Delete Record from Table
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("""--sql
    DELETE from customers WHERE rowid = (?)
    --endsql""", id)

    # Commit our command 
    conn.commit()

    #Close our connection
    conn.close()
```
`our_app.py`
```python
import database

database.delete_one('6')
```
### 18. Add Many Records Function
`database.py`
```python
# Add many records to table
def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("""--sql
    INSERT INTO customers VALUES (?,?,?)
    --endsql""", (first, last, email))

    # Commit our command 
    conn.commit()

    #Close our connection
    conn.close()
```
`our_app.py`
```python
import database

database.add_many(stuff)
```
### 19. Where Clause Function
`database.py`
```python
# Lookup with where
def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("""--sql
    SELECT rowid, * FROM customers WHERE email = (?)
    --endsql""", (email))

    # Commit our command 
    conn.commit()

    #Close our connection
    conn.close()
```
`our_app.py`
```python
import database

database.email_lookup("john@codemy.com")
```