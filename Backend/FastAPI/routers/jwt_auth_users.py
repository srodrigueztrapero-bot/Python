from fastapi import Depends, FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCES_TOKEN_DURATION = 30
SECRET_KEY = "tu_clave_secreta_muy_larga"

app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")
crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    username: str
    fullname: str
    email: str
    disable: bool

class UserDB(User):
    password: str

users_db = {
    "sarayasecas": {
        "username": "sarayasecas",
        "fullname": "saray rodriguez",
        "email": "saray@example.com",
        "disable": False,
        "password": "$2a$12$K1BAfNWvsvHdZScdzY.a0u.IheqiwPONdQdW11helQYSZJH1kT8ry"
    },
    "martinmoreno": {
        "username": "martinmoreno",
        "fullname": "martin moreno",
        "email": "martin@example.com",
        "disable": False,
        "password": "$2a$12$M5sVtkhvc06ioEVvfiYsgOTF/kqbIqcIZ3.9.2C1mDNEK0IQ5z6Du"
    }
}

def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

async def current_user(token: str = Depends(oauth2)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="credenciales inválidas")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="credenciales inválidas")
    
    user = search_user(username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="usuario no encontrado")
    if user.disable:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="usuario inactivo")
    return user

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="usuario incorrecto")
    
    user = search_user_db(form.username)
    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="contraseña incorrecta")
    
    # ← Aquí estaba el error: hay que codificar el token con jwt.encode
    access_token = jwt.encode(
        {"sub": user.username,
         "exp": datetime.utcnow() + timedelta(minutes=ACCES_TOKEN_DURATION)},
        SECRET_KEY,
        algorithm=ALGORITHM
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user