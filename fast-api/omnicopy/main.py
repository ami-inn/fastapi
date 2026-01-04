"""FastAPI application for Omnicopy."""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    """Return a welcome message."""
    return {"message": "Welcome to the Omnicopy API!"}

