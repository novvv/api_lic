from falcon_rest.db import initialize_db
from .base_model import BaseModel
from .settings import DB_CONN_STRING, CREATE_TABLES
from .import create_app


#db = initialize_db(DB_CONN_STRING, BaseModel,db_label='lic')
db = initialize_db(DB_CONN_STRING, BaseModel)

if CREATE_TABLES or True:
    db.create_tables()

app = create_app()

# print (app)
