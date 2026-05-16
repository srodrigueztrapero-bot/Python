from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# uvicorn users:app --reload

# entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int

users_list = [User(id=1, name="Rodriguez", surname="Saray", age=38),
              User(id=2, name="martin", surname="moreno", age=25),
              User(id=3, name="mouredev", surname="dev", age=40)]

@app.get("/usersjson")
async def usersjson():
    return [{"id": 1, "name": "saray", "surname": "rodriguez", "age": 30}, 
            {"id": 2, "name": "martin", "surname": "moreno", "age": 25},
            {"id": 3, "name": "mouredev", "surname": "dev", "age": 40}]    
    

# path params
#     
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

@app.get("/user/")
async def users():
    return users_list
    
# query params
   
@app.get("/userquery/")
async def user(id: int):
    return search_user(id)

def search_user(id: int):    
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        raise HTTPException(status_code=404, detail="User not found")


@app.post("/user/", status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="User already exists")
        
    else:
        users_list.append(user)
        return user  
    

@app.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
        
        if not found:
            return {"error": "no actualizado, usuario no encontrado"}

    return user

@app.delete("/user/{id}")
async def user(id: int):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
        
    if not found:
        return {"error": "no eliminado, usuario no encontrado"}

    return {"message": "Usuario eliminado"}