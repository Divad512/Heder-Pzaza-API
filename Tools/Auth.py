import functools, os
from fastapi import HTTPException, Request, Depends, Header

from Tools.DB import read_data

pathToJson = os.path.join(os.path.dirname(__file__), '..', 'Json', 'Settings.json')



from private import NORMAL_TOKEN as TOKEN


def require_token(func):
    @functools.wraps(func)
    async def wrapper(*args, request: Request = Depends(), **kwargs):
        jsonData = read_data(pathToJson)
        DISABLE_TOKEN = jsonData['Disable-Token']

        x_token: str = request.headers.get("x-token")
        if x_token != TOKEN:
            if not DISABLE_TOKEN:
                raise HTTPException(status_code=401, detail="Unauthorized")
        return func(*args, request=request, **kwargs)
    return wrapper