from fastapi import APIRouter


birthday_api_router = APIRouter()

@birthday_api_router.get("/service/getage")
async def get_birthday(year : int):
    if(year<=0):
        return {"age":"Your input low year"}
    elif(year>2565):
        return {"age":"Your input over year"}
    else:
        return {"age": 2565-year}