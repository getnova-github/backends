from fastapi import FastAPI

app = FastAPI()

completions = ["Completion 1", "Completion 2", "Completion 3"]

@app.get("/brainwave/v1/chat/completions")
def get_completions():
    return {"completions": completions}