from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.exception_handlers import request_validation_exception_handler
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from app.database import async_session_maker

# ✅ IMPORT CORRECT DES ROUTERS
from app.api.routers.auth import router as auth_router
from app.api.routers.members import router as members_router
from app.api.routers.notifications import router as notifications_router
from app.api.routers.responsable import router as responsable_router


app = FastAPI(
    title="Mutuelle Main de Compassion UMOJA API",
    version="1.0.0",
)

# ======================
# CORS
# ======================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # À restreindre en production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ======================
# ROUTERS
# ======================
app.include_router(auth_router)
app.include_router(members_router)
app.include_router(notifications_router)
app.include_router(responsable_router)

# ======================
# DB SESSION MIDDLEWARE
# ======================
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    async with async_session_maker() as session:
        request.state.db = session
        try:
            response = await call_next(request)
        except Exception:
            return JSONResponse(
                status_code=HTTP_500_INTERNAL_SERVER_ERROR,
                content={"detail": "Erreur interne serveur"},
            )
        return response

# ======================
# EXCEPTION HANDLERS
# ======================
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return await request_validation_exception_handler(request, exc)

# ======================
# ROOT
# ======================
@app.get("/")
async def root():
    return {"message": "API Mutuelle Main de Compassion UMOJA opérationnelle"}
