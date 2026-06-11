# users ={
#     "sooya@gmail.com":"12345677"
#   }

# email = input("enter email:")
# password = input("enter password:")

# if email in users and users[email] == password:
#     print("login succcesfully")
# else:
#     print("invalud login")

from fastapi import FastAPI,HTTPException,Header
from pydantic import BaseModel
from passlib.context import CryptContext
import sqlite3
import uuid

app=FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"])

sessions = {}
#database
conn = sqlite3.connect("app.db",check_same_thread = False)
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS )
