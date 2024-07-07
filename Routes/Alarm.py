from fastapi import APIRouter, Request, HTTPException
import os
from Tools.DB import read_data, write_data
from Tools.Auth import require_token

JSON_FILE_NAME = "Alarm.json"
Alarm = APIRouter()



@Alarm.get("/greet")
def greet(request: Request):
    return {"message": 'The "Alarm" is working'}




@Alarm.get('/get')
@require_token
def getStatus(request: Request):
 
    pathToJson = os.path.join(os.path.dirname(__file__), '..', 'Json', JSON_FILE_NAME)  # This goes to the ./Routes, then the (..) goes back one and then switches to Json and then Alarm.json; Then makes it one string    
    status = read_data(pathToJson)

    return status

@Alarm.get('/change')
@require_token
def change(request: Request, armed: bool = None, working: bool = None):
    
    if armed == None and working == None:
        raise HTTPException(status_code=400, detail={'Error': 'Please enter an armed update or a working update', 'Usage': '/change?armed=true | /change?working=true'})
        #return {'Error': 'Please enter an armed update or a working update', 'Usage': '/change?armed=true | /change?working=true'}

    pathToJson = os.path.join(os.path.dirname(__file__), '..', 'Json', JSON_FILE_NAME)  # This goes to the ./Routes, then the (..) goes back one and then switches to Json and then Alarm.json; Then makes it one string    
    status = read_data(pathToJson)

    returnMessage = ""

    if armed is not None:
        if str(status['isArmed']).lower() == str(armed).lower():
            returnMessage = 'Nothing changed'
        else:
            if str(armed).lower() == 'false': status['isArmed'] = False
            else: status['isArmed'] = True

            returnMessage = f'isArmed changed from {not armed} to {armed}'

    if working is not None:
        if str(status['isWorking']).lower() == str(working).lower():
            returnMessage = 'Nothing changed'
        else:
            if str(working).lower() == 'false': status['isWorking'] = False
            else: status['isWorking'] = True

            returnMessage = f'isWorking changed from {not working} to {working}'

    write_data(pathToJson, status)

    return returnMessage