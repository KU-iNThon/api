from fastapi import FastAPI

from fastlib.view import user


app = FastAPI()
app.include_router(user.router, tags=["user"])
