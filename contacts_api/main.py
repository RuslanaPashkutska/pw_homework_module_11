from fastapi import FastAPI
from routes import router


app = FastAPI(
    title="Contacts API",
    description="API for saving and searching contacts with birthday support",
    version="1.0.0"
)
app.include_router(router)