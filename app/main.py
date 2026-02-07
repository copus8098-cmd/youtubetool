from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import audio, video, thumbnail, transcript

app = FastAPI(title="YouTube Toolkit")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(audio.router)
app.include_router(video.router)
app.include_router(thumbnail.router)
app.include_router(transcript.router)
