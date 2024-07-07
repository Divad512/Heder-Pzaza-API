from fastapi import APIRouter, Request, HTTPException
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
def changeStatus(request: Request, temp: int = None, state: bool = None):

    if temp == None and state == None:
        raise HTTPException(status_code=400, detail={'Error': 'Please enter a temp or a state', 'Usage': '/change?temp=25 | /change?state=true'})

    pathToJson = os.path.join(os.path.dirname(__file__), '..', 'Json', JSON_FILE_NAME)  # This goes to the ./Routes, then the (..) goes back one and then switches to Json and then Ac.json; Then makes it one string    
    status = read_data(pathToJson)

    oldTemp = status['temp']
    returnMessage = ""

    if temp:
        if status['temp'] == temp:
            returnMessage = 'Nothing changed'
        else:
            if temp < 16 or temp > 30:
                raise HTTPException(status_code=400, detail={'Error': 'The number has to be above 15 and below 31 (16-30)'})
            status['temp'] = temp
            returnMessage =  f'Temp changed from {oldTemp} to {temp}'

    if state is not None: # have to add the None here because state could be also set to false... (took me a while to find dat)
        if str(status['state']).lower() == str(state).lower():
            returnMessage = 'Nothing changed'
        else:
            if str(state).lower() == 'false': status['state'] = False
            else: status['state'] = True

            returnMessage = f'State changed from {not state} to {state}'

    write_data(pathToJson, status)

    return returnMessage