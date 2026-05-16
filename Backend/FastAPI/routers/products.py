from fastapi import APIRouter

router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses={404: {"message": "Not found"}})

products_list = [
    {"id": 1, "name": "Producto1"},
    {"id": 2, "name": "Producto2"},
    {"id": 3, "name": "Producto3"},
]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def product(id: int):
    for product in products_list:
        if product["id"] == id:
            return product
    return {"error": "Producto no encontrado"}
