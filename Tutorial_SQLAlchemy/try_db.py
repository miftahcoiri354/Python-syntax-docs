import sqlite3

#conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('customer.db')

# Create a cursor
c = conn.cursor()

# Create a Table
query = """--sql
        CREATE TABLE customers2 (
                first_name text, 
                last_name text,
                email text)
        --endsql"""

# Insert a Value into Customer Table
query = """--sql
        INSERT INTO customers 
        VALUES ('Merry', 'Brown', 'john3@codemy.com')
        --endsql"""

# Insert many customers
many_customers = [('Wes', 'brown', 'Wes@brown.com'),
                 ('Steph', 'Kews', 'steph@kewh.com'),
                 ('Dan', 'Pas', 'dan@pas.com')]

# Execute Many Data
query = """--sql 
        INSERT INTO customers 
        VALUES (?,?,?)
        --endsql"""

# Query the Database
query = """--sql 
        SELECT rowid, * FROM customers
        --endsql"""

# Query the Database
query = """--sql 
        SELECT * FROM customers
        WHERE last_name = 'Elder'
        --endsql"""

# Update Records
query = """--sql 
        UPDATE customers 
        SET first_name = 'Bob'
        WHERE last_name = 'Elder'
        --endsql"""

# Delete Records
query = """--sql 
        DELETE FROM customers 
        WHERE rowid = 6
        --endsql"""

# Query the Database - Order by
query = """--sql 
        SELECT rowid, * FROM customers
        ORDER BY rowid DESC
        --endsql"""

# Query the Database
query = """--sql 
        SELECT rowid, * FROM customers
        WHERE last_name LIKE 'Br%'
        OR rowid = 3
        --endsql"""

# Query the Database - Limit
query = """--sql 
        SELECT rowid, * FROM customers
        ORDER BY rowid DSC LIMIT 2 
        --endsql"""

# Query the Database - Limit
query1 = """--sql 
        DROP TABLE customers
        --endsql"""

# Execute Query
c.execute(query)
#c.executemany(query, many_customers)
#c.fetchone()
#c.fetchmany(3)
#print(c.fetchall())

items = c.fetchall()

print("NAME " + "\t\tEMAIL")
print("_______" + "\t\t" + "_________")
for item in items:
        print(item[0]+" "+item[1]+"\t\t"+item[2])

print('Command Executed Succesfully...')

# Commit our command
conn.commit()

# Close our Connection
conn.close()