from fastapi import FastAPI

from fastlib.view import group, user


app = FastAPI()
app.include_router(user.router, tags=["user"])
app.include_router(group.router, tags=["group"])
