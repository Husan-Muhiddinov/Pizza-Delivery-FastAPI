from pydantic import BaseModel
from typing import Optional

class SignUpModel(BaseModel):
    id:Optional[int]
    username:str
    email:str
    password:str
    is_staff:Optional[bool]
    is_active:Optional[bool]

    class Config:
        orm_mode=True
        schema_extra={
            'example':{
                "username":"Husan",
                "email":"khusanmukhiddinov43@gmail.com",
                "password":"password",
                "is_staff":False,
                "is_active":True,
            }
        }


class Settings(BaseModel):
    authjwt_secret_key:str='54e744d69041ab99c7ee820b53604b14f0e04ff0fec41fe8d5d2f6a6fa16074f'


class LoginModel(BaseModel):
    username:str
    password:str