
from fastapi import Request, HTTPException, status


def get_current_user(
        request: Request
):
    username = request.cookies.get("username")

    if username is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    return {"username": username}
