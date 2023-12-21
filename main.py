import os
from fastapi import FastAPI,Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
import uvicorn
from models.data_model import DataModel
from models.user_model import UserModel
from rdf_functions.create_rdf import create_rdf
from rdf_functions.get_all_locations import getAllLocations
from rdf_functions.add_new_location import addNewLocation
from rdf_functions.delete_location import deleteLocation
from rdf_functions.delete_all_locations import deleteAllLocations


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}




@app.post("/create")
async def create(user: UserModel):
    if(os.path.exists('./rdf_files/'+user.name+'.rdf')):
        return Response(status_code=201)
    create_rdf(user)
    return Response(status_code=201)

@app.post("/rdf")
def get_rdf(user: UserModel):    
    if(os.path.exists('./rdf_files/'+user.name+'.rdf')):
        file = open('./rdf_files/'+user.name+'.rdf',"r").read()
        return PlainTextResponse(content=file)
    else:
        return PlainTextResponse(content="")

@app.post("/getalllocations")
async def getalllocations(user: UserModel):
    locations = getAllLocations(user)
    return locations

@app.post("/addnewlocation")
async def addnewlocation(data: DataModel):
    addNewLocation(data.user, data.location)
    return Response(status_code=201)

@app.delete("/deletelocation")
async def deletelocation(data: DataModel):
    deleteLocation(data.user,data.location)
    return Response(status_code=201)

@app.delete("/deletealllocations")
async def deletealllocations(user: UserModel):
    deleteAllLocations(user)
    return Response(status_code=201)
    
    
    
    
    
if __name__ == "__main__":
    config = uvicorn.Config("main:app",host="0.0.0.0", port=10000, log_level="info")
    server = uvicorn.Server(config)
    server.run()

