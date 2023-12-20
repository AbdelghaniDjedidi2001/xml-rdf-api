import os
from fastapi import FastAPI,Response,File
from fastapi.responses import PlainTextResponse
from models.data_model import DataModel
from models.user_model import UserModel
from rdf_functions.create_rdf import create_rdf
from rdf_functions.get_all_locations import getAllLocations
from rdf_functions.add_new_location import addNewLocation
from rdf_functions.delete_location import deleteLocation
from rdf_functions.delete_all_locations import deleteAllLocations
from rdf_functions.get_number_of_locations import getNumberOfLocations
from os import read

app = FastAPI()


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