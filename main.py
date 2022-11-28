from fastapi import FastAPI
import uvicorn



@app.get("/")

def root():
    return {"message": "Hello world"}

@app.get("/say/{data}")
def say(data: str,q: int):
    return {"data": data, "item": q}



if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")