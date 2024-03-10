from fastapi import APIRouter
root_router = APIRouter()







from modules.users.router import user_router
root_router.include_router(user_router)
