from rdflib import Graph, Namespace, Literal, XSD
from rdflib.namespace import RDF, RDFS
from models.location_model import LocationModel
from models.user_model import UserModel
from rdf_functions.get_number_of_locations import getNumberOfLocations


def deleteLocation(user:UserModel,location_model:LocationModel):
    model = Graph()
    model.parse("rdf_files/"+user.name+".rdf", format="xml")
    exNS = Namespace("http://example.org/")
    userLocationRecord = model.resource(exNS[user.name+"LocationRecord"])

    for location in model.subjects(RDF.type, exNS.Location):
        print(location)
        if str(model.value(location,exNS.hasTimestamp)) == location_model.timestamp:
            print("found")
            locationToDelete = model.resource(location)
            locationToDelete.remove(RDF.type, exNS.Location)
            locationToDelete.remove(exNS.hasTimestamp, Literal(location_model.timestamp, datatype=XSD.dateTime))
            locationToDelete.remove(exNS.hasLatitude, Literal(location_model.latitude, datatype=XSD.float))
            locationToDelete.remove(exNS.hasLongitude, Literal(location_model.longitude, datatype=XSD.float))
            locationsCount = getNumberOfLocations(user)
            userLocationRecord.set(exNS.hasLocationCount,Literal(locationsCount-1))
            userLocationRecord.remove(exNS.hasLocation, location)
            break
    model.serialize(destination="rdf_files/"+user.name+".rdf", format="xml")
    model.close()
    return True