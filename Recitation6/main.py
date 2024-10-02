from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Food(BaseModel):
    id: int # id for food item
    name: str # name of food item
    price: float # price of food item


food_instance = [
    Food(id=1, name="ham", price=5.2), #first food item
    Food(id=2, name="bread", price=2.5) #second food item
]




@app.get("/")
def read_all():
    return food_instance


@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in food_instance:
        if item.id == item_id:
            return item
    return "Item not Found!"


@app.post("/items")
def write_item(food: Food):
    food_instance.append(food)
    return food_instance


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Food):
    is_found = False
    for index, instance in enumerate(food_instance):
        if instance.id == item_id:
            food_instance[index] = Food(id=item.id, name=item.name, price=item.price)
            is_found = True
            break
    if not is_found:
        return "Item not Found!"

    return food_instance


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    is_found = False
    for index, instance in enumerate(food_instance):
        if instance.id == item_id:
            del food_instance[index]
            is_found = True
            break
    if not is_found:
        return "Item not Found!"

    return food_instance


# Changes the price of an item by name using Food class
@app.put("/items/{item_name}/price")
def update_item_price(item_name: str, item: Food):
    is_found = False
    for instance in food_instance:
        if instance.name == item_name:
            instance.price = item.price  # Only updating the price
            is_found = True
            break
    if not is_found:
        return "Item not Found!"

    return food_instance
