"""
uvicorn main:app --reload --port 8000
"""

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse
import uvicorn

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return "<h1>API - сервис по приборам учёта</h1>"


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000)
