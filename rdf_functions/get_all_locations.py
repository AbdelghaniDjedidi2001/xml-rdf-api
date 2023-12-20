from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from models.location_model import LocationModel
from models.user_model import UserModel

def getAllLocations(user_model:UserModel):
    model = Graph()
    model.parse("rdf_files/"+user_model.name+".rdf", format="xml")
    exNS = Namespace("http://example.org/")
    locations:LocationModel = []
    for location in model.subjects(RDF.type, exNS.Location):
        locations.append(LocationModel(
            latitude=float(model.value(location,exNS.hasLatitude)),
            longitude=float(model.value(location,exNS.hasLongitude)),
            timestamp=model.value(location,exNS.hasTimestamp)
        ))
    return locations        