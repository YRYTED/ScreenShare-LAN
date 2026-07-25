from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

import socket
import asyncio
import base64
import qrcode
import io

from capture import capture_screen


app = FastAPI()


app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except:
        ip = "127.0.0.1"

    s.close()

    return ip



@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    with open("templates/index.html", "r", encoding="utf-8") as f:
        html = f.read()

    ip = get_ip()

    html = html.replace(
        "{{IP}}",
        ip
    )

    return html



@app.websocket("/stream")
async def stream(websocket: WebSocket):

    await websocket.accept()

    while True:

        frame = capture_screen()

        encoded = base64.b64encode(
            frame
        ).decode()

        await websocket.send_text(encoded)

        await asyncio.sleep(0.05)