from fastapi import APIRouter

age_api_router = APIRouter()

@age_api_router.get("/service/getage")
async def get_age(year:int):
    if(year<=0):
        return {"age": "your input too less"}
    elif(year>2565):
        return {"age":"your input too over"}
    else:
        return {"age": 2565-year}


