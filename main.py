import uvicorn
from fastapi import FastAPI, Body


from heandlers.heandlers import router


app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)



