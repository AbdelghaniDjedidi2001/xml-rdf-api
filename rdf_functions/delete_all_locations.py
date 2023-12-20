from rdflib import Graph, Namespace, Literal, XSD
from rdflib.namespace import RDF, RDFS
from models.location_model import LocationModel
from models.user_model import UserModel
from rdf_functions.delete_location import deleteLocation
from rdf_functions.get_number_of_locations import getNumberOfLocations


def deleteAllLocations(user:UserModel):
    model = Graph()
    model.parse("rdf_files/"+user.name+".rdf", format="xml")
    exNS = Namespace("http://example.org/")
    for location in model.subjects(RDF.type, exNS.Location):
        locationToDelete = LocationModel(
            latitude=float(model.value(location,exNS.hasLatitude)),
            longitude=float(model.value(location,exNS.hasLongitude)),
            timestamp=model.value(location,exNS.hasTimestamp)
        )
        deleteLocation(user,locationToDelete)
    return True