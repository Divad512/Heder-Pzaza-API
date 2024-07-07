import functools
from fastapi import HTTPException, Request, Depends, Header

TOKEN = 'dookie-is-hot'
DISABLE_TOKEN = True 

def require_token(func):
    @functools.wraps(func)
    async def wrapper(*args, request: Request = Depends(), **kwargs):
        x_token: str = request.headers.get("x-token")
        if x_token != TOKEN:
            if not DISABLE_TOKEN:
                raise HTTPException(status_code=401, detail="Unauthorized")
        return func(*args, request=request, **kwargs)
    return wrapper