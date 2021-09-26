from typing import Optional

import os
import requests

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://serverless-arch-frontend.pages.dev/", "localhost"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root(token: str = ""):
    if token == "":
        return {
            "Status": 400,
            "Messages": "Bad Request",
            "Data" : "Token not valid"   
        }
        
    url = "https://www.google.com/recaptcha/api/siteverify?secret={}&response={}".format(os.getenv('RECAPTCHA_SERVER'), token)
    
    r = requests.post(url=url)
    data = r.json()
    
    print(data)
    
    if data["success"] == False:
        return {
            "Status": 403,
            "Messages": "Captcha not valid",
            "Data": ""
        }
        
    return {"Status" : 200,
            "Messages" : "Success",
            "Data" : "Halo ini dari serverless function di heroku lhoo"}