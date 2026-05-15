from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1810",
        database="connect_api",
        port=3306
    )
    
class user(BaseModel):
    User_Id : int
    Username : str
    Mobile_Number : str
    Entry_Date : str
    
@app.post("/user")
def insert_user(User:user):
    db = get_db()
    cursor = db.cursor()
    
    sql = "INSERT INTO user (User_Id, Username, Mobile_Number, Entry_Date) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (User.User_Id, User.Username, User.Mobile_Number, User.Entry_Date))
    db.commit()

    cursor.close()
    db.close()

    return {"message": "User added"}

@app.get("/user")
def view_user():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM user")
    data = cursor.fetchall()

    cursor.close()
    db.close()

    return data

class unit(BaseModel):
    Unit_Id : int
    Unit : str

@app.post("/unit")
def insert_unit(Unit:unit):
    db = get_db()
    cursor = db.cursor()
    
    sql = "INSERT INTO unit (Unit_Id, Unit) VALUES (%s, %s)"
    cursor.execute(sql, (Unit.Unit_Id, Unit.Unit))
    db.commit()

    cursor.close()
    db.close()

    return {"message": "Unit added"}

@app.get("/unit")
def view_unit():
    db = get_db()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM unit")
    data = cursor.fetchall()

    cursor.close()
    db.close()

    return data