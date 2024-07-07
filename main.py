# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json, os
import datetime

app = FastAPI()

from Routes.Light import roomLight
from Routes.Ac import Ac
from Routes.Alarm import Alarm


app.include_router(prefix='/light', router=roomLight)
app.include_router(prefix='/ac', router=Ac)
app.include_router(prefix='/alarm', router=Alarm)

@app.get('/')
async def mainPage():
    return 'hola'


@app.get("/time")
async def timePage():
    x = datetime.datetime.now()

    time = x.time()
    date = x.date()

    return {'time': time, 'date': date}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)