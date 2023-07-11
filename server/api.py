from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root():
    return JSONResponse({"message": "Welcome to Hello World"}, status_code=200)
