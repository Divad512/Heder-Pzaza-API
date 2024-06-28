from fastapi import APIRouter, Request
import os
from Tools.DB import read_data, write_data
from Tools.Auth import require_token

JSON_FILE_NAME = "Ac.json"
Ac = APIRouter()



@Ac.get("/greet")
def greet(request: Request):
    return {"message": "The \"Ac\" is working"}




@Ac.get('/get')
@require_token
def getStatus(request: Request):
 
    pathToJson = os.path.join(os.path.dirname(__file__), '..', 'Json', JSON_FILE_NAME)  # This goes to the ./Routes, then the (..) goes back one and then switches to Json and then Ac.json; Then makes it one string    
    status = read_data(pathToJson)

    return status


@Ac.get('/change')
@require_token
def changeStatus(request: Request, mode: str = None):

    if mode == None:
        return {'Error': 'Please enter a mode'}

    pathToJson = os.path.join(os.path.dirname(__file__), '..', 'Json', JSON_FILE_NAME)  # This goes to the ./Routes, then the (..) goes back one and then switches to Json and then Ac.json; Then makes it one string    
    status = read_data(pathToJson)

    if int(mode) > 15 and int(mode) < 31:
        return 'is number valid'
    if mode.lower() in ['true', 'false']:
        return 'is string'

    #data = {
    #    "status": not status['sate']
    #}
#
    #write_data(pathToJson, data)
    print(mode.format())
    return f"printed"