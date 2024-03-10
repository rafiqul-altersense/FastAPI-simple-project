from fastapi import APIRouter, Depends, Request, Response
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from utils.auth import get_current_username
from fastapi.responses import HTMLResponse
from settings import templates

user_router = APIRouter(tags=["User"])


@user_router.get("/profile-data")
async def read_item(credentials: HTTPBasicCredentials = Depends(get_current_username)):
    return {"username": credentials.username, "password": credentials.password}


@user_router.get("/profile", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        request=request, name="users/profile.html", context={"username": "Rafiqul"}
    )


@user_router.post("/profile/{username}")
async def read_item(username: str, response: Response):
    response.set_cookie(key="username", value=username)
    return {"username": username}
