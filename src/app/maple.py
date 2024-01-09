from litestar import Litestar, get


@get("/")
async def index() -> str:
    return "Hello, world!"

def Maple() -> Litestar: 
    return Litestar([index])