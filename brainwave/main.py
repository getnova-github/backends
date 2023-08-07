from fastapi import FastAPI

app = FastAPI()

@app.get("/brainwave/v1/chat/completions")
def get_completions():
    return {"message": "Endpoint working correctly"}