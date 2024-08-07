from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi.middleware.gzip import GZipMiddleware
from entrypoints.routers import auth_routers


version = "1.2"
title= "AUTH"
description="This is a custom API built with FastAPI."

app = FastAPI(
    title=title,
    description=description,
    version=version
)


# # CORS
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Configurar GZipMiddleware con un tamaño mínimo de 100 MB para comprimir respuestas
app.add_middleware(GZipMiddleware, minimum_size=1000000)
app.max_request_size = 100000000  # 100 MB en bytes

  
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        errors.append( 
            {
                "loc": error["loc"],
                "msg": error["msg"],
                "type": error["type"],
            }
        )
    return JSONResponse(status_code=HTTP_422_UNPROCESSABLE_ENTITY, content={"detail": errors})

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(status_code=exc.status_code, content={"details": exc.detail})

@app.exception_handler(Exception)
async def generic_exception_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": "Ha ocurrido un error inesperado"})

@app.get("/")
async def root():
    return True


app.include_router(auth_routers.router, prefix="/api/auth", tags=["AUTH"])