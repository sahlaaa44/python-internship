from pydantic import BaseModel

class usercreate(BaseModel):
    email : str
    password : str

class taskcreate(BaseModel):
    title:str
    status:str