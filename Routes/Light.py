from fastapi import APIRouter, Request
import os
from Tools.DB import read_data, write_data
from Tools.Auth import require_token

JSON_FILE_NAME = "Light.json"
roomLight = APIRouter()



@roomLight.get("/greet")
def greet(request: Request):
    return {"message": 'The "Light" is working'}




@roomLight.get('/get')
@require_token
def getStatus(request: Request):
 
    pathToJson = os.path.join(os.path.dirname(__file__), '..', 'Json', JSON_FILE_NAME)  # This goes to the ./Routes, then the (..) goes back one and then switches to Json and then Light.json; Then makes it one string    
    status = read_data(pathToJson)

    return status


@roomLight.get('/change')
@require_token
def changeStatus(request: Request):

    pathToJson = os.path.join(os.path.dirname(__file__), '..', 'Json', JSON_FILE_NAME)  # This goes to the ./Routes, then the (..) goes back one and then switches to Json and then Light.json; Then makes it one string    
    status = read_data(pathToJson)

    data = {
        "state": not status['state']
    }

    write_data(pathToJson, data)

    return f"changed to {not status['state']}"