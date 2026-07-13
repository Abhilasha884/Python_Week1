from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,EmailStr

app=FastAPI()

class user_request(BaseModel):
    name:str
    password:str
    email:EmailStr
    is_active:bool

class user_response(BaseModel):
    name:str
    email:EmailStr

users=[]

@app.get('/users')
def get_users():
    return users

@app.get('/users/{User_name}')
def get_user(User_name:str):
    for user in users:
        if user.name==User_name:
            return user
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )

@app.post('/users/',response_model=user_response)

def create_user(user:user_request):
    for u in users:
        if u.name==user.name:
            raise HTTPException(
                status_code=400,
                detail="User already available"
            )
    users.append(user)
    return user
    

