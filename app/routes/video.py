from fastapi import APIRouter
from services.ytdlp import run, DOWNLOAD_DIR
import os

router = APIRouter(prefix="/video", tags=["Video"])

@router.get("/")
def download_video(url: str):
    output = os.path.join(DOWNLOAD_DIR, "%(title).50s.%(ext)s")

    cmd = [
        "yt-dlp",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best",
        "--merge-output-format", "mp4",
        "-o", output,
        url
    ]

    run(cmd)
    return {"status": "ok", "type": "video"}
