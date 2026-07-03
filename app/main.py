from fastapi import FastAPI
from app.api.routes.auth import router as auth
#from app.api.routes.url import router as urls
#from app.api.routes.admin import router as admin
#from app.api.routes.dashboard import router as dashboard

app = FastAPI(
    title="Website For Login and Register",
    version="1.0.0"
)


app.include_router(auth, prefix="/api/v1/auth", tags=["Auth"])
#app.include_router(urls, prefix="/api/v1/urls", tags=["URLs"])
#app.include_router(admin, prefix="/api/v1/admin", tags=["Admin"])
#app.include_router(dashboard, prefix="/api/v1/dashboard", tags=["Dashboard"])

@app.get("/health")
def health():
    return {"status": "healthy"}