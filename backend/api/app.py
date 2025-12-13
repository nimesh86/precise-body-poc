from fastapi import FastAPI, HTTPException
from backend.main import generate_character
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Precise Human Body Generation API",
    version="1.0",
)


@app.post("/api/v1/generate")
def generate(payload: dict):
    try:
        return generate_character(payload)
    except Exception as e:
        # POC-level error handling
        raise HTTPException(status_code=400, detail=str(e))


# STATIC FILES AFTER API
app.mount("/outputs", StaticFiles(directory="outputs"), name="outputs")
app.mount("/ui", StaticFiles(directory="webui/public", html=True), name="ui")