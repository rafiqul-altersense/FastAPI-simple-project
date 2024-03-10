from modules.users.router import user_router
from fastapi import APIRouter


root_router = APIRouter()


@root_router.get("/")
async def read_root():
    return {"message": "Hello World"}






root_router.include_router(user_router)
