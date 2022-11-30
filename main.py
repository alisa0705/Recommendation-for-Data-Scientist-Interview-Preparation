from fastapi import FastAPI
import uvicorn
from alisa_library.create import viedo_suggestions
from alisa_library.create import channels_Search
from alisa_library.create import playlists_Search

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to the youtube video suggestion recommendation! Please select: /viedo_suggestions or /channels_Search or /playlists_Search"}

@app.get("/viedo_suggestions/{search}")
async def viedo_suggestions(search: str):
    '''Get the youtube video suggestion'''
    output = viedo_suggestions(search)
    return {"output": output}


@app.get("/channels_Search/{search}")
async def channels_Search(search: str):
    '''Search only channels'''
    output = channels_Search(search)
    return {"output": output}

@app.get("/playlists_Search/{search}")
async def playlists_Search(search: str):
    '''Search only playlists'''
    output = playlists_Search(search)
    return {"output": output}
        

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")