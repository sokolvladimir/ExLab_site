from fastapi import FastAPI, APIRouter

from api.handlers import user_router

app = FastAPI(title="ExLab bot API")

main_api = APIRouter()

main_api.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(main_api, prefix="/api/v1")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
