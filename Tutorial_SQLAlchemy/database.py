import sqlite3

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