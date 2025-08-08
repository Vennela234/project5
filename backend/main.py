from fastapi import FastAPI
from backend.routes import content

app = FastAPI()

# Register the router
app.include_router(content.router, prefix="/api/content")
