from fastapi import APIRouter,Header,HTTPException
from passlib.context import CryptContext
# from schemas import useregister
# from database import get_connection
import uuid
router = APIRouter()

pwd_context = CryptContext(
    schemes = ["bcrypt"],
    deprecated = "auto"
)
sessions = {}

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password,hashed):
    return pwd_context.verify(
        password,
        hashed
    )

def create_token():
    return str(uuid.uuid4())

def get_current_user(
        authorization: str = Header(None)
):
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail = "token missing"
        )
    
    token = authorization.replace(
        "bearer",""
    )
    
    if token not in sessions:
        raise HTTPException(
            status_code=401,
            detail = "invalid token"
        )
    
    return sessions[token]