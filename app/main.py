from typing import List
from fastapi import FastAPI

from app import services
from app.schema import UserIn, BaseResponse, UserListOut

app = FastAPI()


@app.get("/")
async def index():
    """
    Index route for our application
    """
    return {"message": "Welcome To Nimap Infotech Pvt Ltd ;)"}


@app.post("/users", response_model=BaseResponse)
async def user_create(user: UserIn):
    """
    Add user data to json file
    """
    try:
        services.add_userdata(user.dict())
    except:
        return {"success": False}
    return {"success": True}


@app.get("/users", response_model=UserListOut)
async def get_users():
    """
    Read user data from json file
    """
    return services.read_usersdata()
