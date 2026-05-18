from fastapi import FastAPI
from routers import products, users_api, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

#routers
app.include_router(products.router)
app.include_router(users_api.router)
app.include_router(basic_auth_users.router)
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)
app.mount("/static", StaticFiles(directory="static"), name="static")

# url http://127.0.0.1:8000
# inicia el server con  uvicorn main:app --reload

@app.get("/")
async def root():
    return "Hola FastAPI"

@app.get("/url")
async def get_url():
    return {"url_curso": "https://mouredev.com/python"}