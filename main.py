from fastapi import FastAPI, APIRouter

app = FastAPI(title="ExLab bot API")

main_api = APIRouter()

app.include_router(main_api, prefix="/api/v1")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
