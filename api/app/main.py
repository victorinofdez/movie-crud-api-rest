from fastapi import FastAPI
from routers import users, movies, auth

app = FastAPI(
    title="API de Películas y Usuarios",
    version="1.0.0"
)

app.include_router(users.router)
app.include_router(movies.router)
app.include_router(auth.router)