# main.py

from fastapi import FastAPI, HTTPException, Request
import json, os
import datetime
from Tools.DB import read_data, write_data

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


@app.get('/token')
async def token(request: Request, disable_token: bool = None):
    x_token: str = request.headers.get("x-token")
    from private import ADMIN_TOKEN as admin_token
    if x_token != admin_token:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    pathToJson = os.path.join('Json', 'Settings.json')
    data = read_data(pathToJson)

    returnMessage = "Please add a parameter"

    if disable_token is not None:
        data['Disable-Token'] = disable_token
        returnMessage = f"Changed to {disable_token}"

    write_data(pathToJson, data)

    raise HTTPException(status_code=200, detail=returnMessage)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)