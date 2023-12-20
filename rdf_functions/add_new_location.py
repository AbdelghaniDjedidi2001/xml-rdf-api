from rdflib import Graph, Namespace, Literal
from rdflib.resource import Resource
from rdflib.namespace import RDF, RDFS
from models.location_model import LocationModel
from models.user_model import UserModel
from rdf_functions.get_number_of_locations import getNumberOfLocations
from rdflib.plugins.sparql import prepareUpdate



def addNewLocation(user_model:UserModel,userNewLocation:LocationModel):
    exNS = Namespace("http://example.org/")
    xmls = Namespace("http://www.w3.org/2001/XMLSchema#")

    model = Graph()
    model.parse("rdf_files/"+user_model.name+".rdf", format="xml")
    locationsCount:int = getNumberOfLocations(user_model)
    locationsCount+=1
    newLocation = exNS["Location"+str(locationsCount)]
    
    model.add((newLocation, RDF.type, exNS.Location))
    model.add((newLocation, exNS.hasTimestamp, Literal(userNewLocation.timestamp, datatype=xmls.string)))
    model.add((newLocation, exNS.hasLatitude, Literal(userNewLocation.latitude, datatype=xmls.float)))
    model.add((newLocation, exNS.hasLongitude, Literal(userNewLocation.longitude, datatype=xmls.float)))

    userLocationRecord = exNS[user_model.name+"LocationRecord"]
    model.add((userLocationRecord, exNS.hasLocation, newLocation))
    
    location_record = model.resource(exNS[str(user_model.name)+"LocationRecord"])
    location_record.set(exNS.hasLocationCount,Literal(locationsCount))
   
    model.serialize(destination="rdf_files/"+user_model.name+".rdf", format="xml")
    model.close()

def updateLocationsCount(newLocationsCount:int,user_model:UserModel):
    model = Graph()
    exNS = Namespace("http://example.org/")
    model.parse("rdf_files/"+user_model.name+".rdf", format="xml")
    location_record = model.resource(exNS[str(user_model.name)+"LocationRecord"])
    location_record.set(exNS.hasLocationCount,Literal(newLocationsCount))
    model.serialize(destination="rdf_files/"+user_model.name+".rdf", format="xml")
    model.close()