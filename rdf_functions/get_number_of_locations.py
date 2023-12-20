from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from models.user_model import UserModel
from rdflib.plugins.sparql import prepareQuery


def getNumberOfLocations(userModel:UserModel):
    exNS = Namespace("http://example.org/")
    model = Graph()
    model.parse("rdf_files/"+userModel.name+".rdf", format="xml")
    location_record = model.resource(exNS[str(userModel.name)+"LocationRecord"])
    return int(location_record.value(exNS.hasLocationCount))
