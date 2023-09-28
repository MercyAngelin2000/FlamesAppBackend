from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import flames

app=FastAPI()
app.include_router(flames.router)

origins = [
    "http://localhost:3000", "http://localhost:3001",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"Hai":"Welcome"}