from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Status" : 200,
            "Messages" : "Success",
            "Data" : "Halo ini dari serverless function di heroku lhoo"}