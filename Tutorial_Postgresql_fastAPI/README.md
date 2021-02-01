# learn_fastAPI_postgreSQL
 
 Link Tutorial PostgreSQL+FastAPI: https://www.youtube.com/watch?v=YUuuJPokBf4

Tutorial Install TimescaleDB+PostgreSQL: https://www.open-plant.com/knowledge-base/timescaledb-setup-for-windows-10/

### 1. Create Virtual Environment
```
> pip install -r requirements.txt
> pip install databases[postgresql]
```

### 2. Build Connection String for PostgreSQL
```python

import urllib
import os

host_server = os.environ.get('host_server', 'localhost')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port','5432')))
database_name = os.environ.get('database_name', 'fastapi')
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username','postgres')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password','2345678910Aa')))
ssl_mode = urllib.parse.quote_plus(str(os.environ.get('ssl_mode','prefer')))

DATABASE_URL = "postgresql://{}:{}@{}:{}/{}?sslmode={}".format(db_username, db_password, host_server, db_server_port, database_name, ssl_mode)
#DATABASE_URL = "sqlite:///./test.db"
```

### 3. Setup SQL Alchemy Models & Engine
```python
import sqlalchemy

metadata = sqlalchemy.MetaData()

notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column('text', sqlalchemy.String),
    sqlalchemy.Column('completed', sqlalchemy.Boolean),
)

engine = sqlalchemy.create_engine(
    #DATABASE_URL, connect_args={"check_same_thread":False}
    DATABASE_URL, pool_size=3, max_overflow=0
)

metadata.create_all(engine)
```

### 4. Setup Pydantic Models
```python
from pydantic import BaseModel

class NoteIn(BaseModel):
    text: str
    completed: bool

class Note(BaseModel):
    id: int
    text: str
    completed: bool
```

### 5. Initialize FastAPI
```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI(title="REST API using FastAPI PostgreSQL Async EndPoints")
```

### 6. FastAPI CORS Setup
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"]
)
```

### 7. Setup Database Module
```python
import databases

database = databases.Database(DATABASE_URL)
```

### 8. FastAPI Events Startup Shutdown
```python
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
```

### 9. Implement POST to Create a new note
```python
@app.post("/notes/", response_model= Note)
async def create_note(note: NoteIn):
    query = notes.insert().values(text=note.text, completed=note.completed)
    last_record_id = await database.execute(query)
    return {**note.dict(), "id": last_record_id}
```

### 10. Create Database in PostgreSQL
```
Create Database Similar with Defined in Python File
```

### 11. Run FastAPI using Uvicorn 
```
# Run uvicorn in cmd shell
# TODO: to run this program, type => uvicorn main:app --reload
```

### 12. Insert a Note using CURL
```
# Open new cmd shell and type this code to add new data into database
# TODO: curl -X POST "http://localhost:8000/notes/" ^
# TODO: -H "accept: application/json" ^
# TODO: -H "Content-Type: application/json" ^
# TODO: -d "{\"text\":\"Get Groceries from the store\",\"completed\":false}" -> it will add new data to database
```

### 13. Create GET Method to retrieve a Note data from Database
```python
@app.get("/notes/", response_model=List[Note])
async def read_notes(skip: int =0, take:int=20):
    query = notes.select().offset(skip).limit(take)
    return await database.fetch_all(query)

```

### 14. Implement PUT Method to Update Note
```python
@app.put("/notes/{note_id}", response_model=Note)
async def update_note(note_id: int, payload: NoteIn):
    query = notes.update().where(notes.c.id == note_id).value(text=payload.text, completed=payload.completed)
    await database.execute(query)
    return {**payload.dict(), 'id':note_id}
```

### 15. Implement GET to Retrieve a Note by ID
```python
@app.get("/notes/{note_id}", response_model=Note)
async def read_notes(note_id: int):
    query = notes.select().where(notes.c.id == note_id)
    return await database.fetch_one(query)
```

### 16. Implement DELETE to permanently delete a Note given its ID
```python
@app.delete("/notes/{note_id}")
async def delete_notes(note_id: int):
    query = notes.delete().where(notes.c.id == note_id)
    await database.execute(query)
    return {'message': "Note with id: {} deleted successfully". format(note_id)}
```

### 17. Add Note using CURL
```
# Open new cmd shell and type this code to add new data into database
# TODO: curl -X POST "http://localhost:8000/notes/" ^
# TODO: -H "accept: application/json" ^
# TODO: -H "Content-Type: application/json" ^
# TODO: -d "{\"text\":\"Get Groceries from the store\",\"completed\":false}" -> it will add new data to database
```

### 18. Get Notes Collection using CURL
```
# Open new cmd shell and type this code to retrieve data from database
# TODO: curl -X GET "http://localhost:8000/notes/" 
# TODO: curl -X GET "http://localhost:8000/notes/2" 
```

### 19. Update Note using CURL
```
# Open new cmd shell and type this code to update data in database
# TODO: curl -X PUT "http://localhost:8000/notes/2" ^
# TODO: -H "accept: application/json" ^
# TODO: -H "Content-Type: application/json" ^
# TODO: -d "{\"text\":\"Get Groceries from the store\",\"completed\":false}" -> it will add new data to database
```

### 20. Delete Note using CURL
```
# Open new cmd shell and type this code to delete data from database
# TODO: curl -X DELETE "http://localhost:8000/notes/2" -H "accept: application/json"
```
