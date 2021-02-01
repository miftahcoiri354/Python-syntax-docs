import database

# Add a record to the database, first name, last name, email
#database.add_one("Laura","Smith",'Laura@smith.com')

#Delete record user the row id number 6
#database.delete_one('6')

# Add many data in list
#stuff = [
#    ('Brenda','Smitherton','Brenda@smithon.com'),
#    ('Joshua','Raintree','josh@raintree.com')
#    ]
#database.add_many(stuff)

# Lookup email Address Record
database.email_lookup("john@codemy.com")

#Show all customer data
database.show_all()