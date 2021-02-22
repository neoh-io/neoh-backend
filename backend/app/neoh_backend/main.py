from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from neoh_backend.api.v1.api import api_router
from neoh_backend.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Watch random videos with your friends!",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)

# Set all CORS Enabled Origins
if settings.BACKEND_CORS_ORIGINS: # pragma: no cover
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
app.include_router(api_router, prefix=settings.API_V1_STR)
