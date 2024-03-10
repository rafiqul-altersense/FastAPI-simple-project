from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")



# Common exception handler for all exceptions
@app.exception_handler(Exception)
async def common_exception_handler(request: Request, exc: Exception):
    status_code = getattr(exc, "status_code", 500)
    detail = getattr(exc, "detail", "Internal Server Error")

    return templates.TemplateResponse(
        name="exception/error.html",
        context={"request": request, "status_code": status_code, "detail": detail},
        status_code=status_code,
    )


# Custom exception handler for 404 Not Found
@app.exception_handler(HTTPException)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    return templates.TemplateResponse(
        name="exception/not_found.html",
        context={"request": request, "status_code": exc.status_code, "detail": exc.detail},
        status_code=exc.status_code,
    )

# Custom exception handler for 500 Internal Server Error
@app.exception_handler(Exception)
async def internal_server_error_handler(request: Request, exc: Exception):
    return templates.TemplateResponse(
        name="exception/internal_server_error.html",
        context={"request": request, "error": str(exc)},
        status_code=500,
    )



from settings.routes import root_router
app.include_router(root_router)
