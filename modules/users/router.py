from fastapi import APIRouter, Depends, Request, Response
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from utils.auth import get_current_user
from fastapi.responses import HTMLResponse
from settings import templates

user_router = APIRouter(tags=["User"])


@user_router.get("/profile", response_class=HTMLResponse)
async def read_item(request: Request, user: HTTPBasicCredentials = Depends(get_current_user)):
    # print("user-->", user)
    return templates.TemplateResponse(
        request=request, name="users/profile.html", context={"username": user['username']}
    )


@user_router.get("/profile/{username}")
async def read_item(username: str, response: Response):
    response.set_cookie(key="username", value=username)
    return {"username": username}
