from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from auth.auth_handler import get_current_user
from routes import user_router, auth_router

app = FastAPI(title="FastAPI Auth Demo", description="FastAPI application with user authentication")

# Include routers
app.include_router(auth_router.router, prefix="/auth", tags=["Authentication"])
app.include_router(user_router.router, prefix="/users", tags=["Users"])

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Auth Demo"}

@app.get("/protected")
async def protected_route(current_user: dict = Depends(get_current_user)):
    return {"message": f"Hello {current_user['username']}, this is a protected route"}