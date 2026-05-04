from fastapi import FastAPI


app = FastAPI()
import user_routes
app.include_router(user_routes.router)

@app.get("/")
def home():
    return {"message": "API is running 🚀"}