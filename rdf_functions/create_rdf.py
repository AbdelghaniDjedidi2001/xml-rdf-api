from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from models.user_model import UserModel


def create_rdf(user_model:UserModel):
    exNS = Namespace("http://example.org/")
    xmls = Namespace("http://www.w3.org/2001/XMLSchema#")

    # Create an RDF graph
    model = Graph()
    model.bind("ex", exNS)

    # Define resources
    user_class = exNS.User
    location_class = exNS.Location
    location_record_class = exNS.LocationRecord

    # Define properties
    has_location = exNS.hasLocation
    has_location_record = exNS.hasLocationRecord
    has_timestamp = exNS.hasTimestamp
    has_latitude = exNS.hasLatitude
    has_longitude = exNS.hasLongitude
    has_location_count = exNS.hasLocationCount
    has_email = exNS.hasEmail
    has_password = exNS.hasPassWord

    # Add properties and domains/ranges
    model.add((has_location, RDF.type, RDF.Property))
    model.add((has_location, RDFS.domain, location_record_class))
    model.add((has_location, RDFS.range, location_class))

    model.add((has_location_record, RDF.type, RDF.Property))
    model.add((has_location_record, RDFS.domain, user_class))
    model.add((has_location_record, RDFS.range, location_record_class))

    model.add((has_timestamp, RDF.type, RDF.Property))
    model.add((has_timestamp, RDFS.domain, location_class))
    model.add((has_timestamp, RDFS.range, xmls.string))

    model.add((has_latitude, RDF.type, RDF.Property))
    model.add((has_latitude, RDFS.domain, location_class))
    model.add((has_latitude, RDFS.range, xmls.float))

    model.add((has_longitude, RDF.type, RDF.Property))
    model.add((has_longitude, RDFS.domain, location_class))
    model.add((has_longitude, RDFS.range, xmls.float))

    model.add((has_location_count, RDF.type, RDF.Property))
    model.add((has_location_count, RDFS.domain, location_record_class))
    model.add((has_location_count, RDFS.range, xmls.int))

    model.add((has_email, RDF.type, RDF.Property))
    model.add((has_email, RDFS.domain, user_class))
    model.add((has_email, RDFS.range, xmls.string))

    model.add((has_password, RDF.type, RDF.Property))
    model.add((has_password, RDFS.domain, user_class))
    model.add((has_password, RDFS.range, xmls.string))

    # Add classes
    
    model.add((user_class,RDF.type,RDFS.Class))
    model.add((location_class,RDF.type,RDFS.Class))
    model.add((location_record_class,RDF.type,RDFS.Class))
 
    # Add individual locationRecord for the user
    location_record = exNS[user_model.name + "LocationRecord"]
    model.add((location_record, RDF.type, location_record_class))
    model.add((location_record, has_location_count, Literal(0, datatype=xmls.int)))

    # Add user and connect properties
    user = exNS[user_model.name]
    model.add((user, RDF.type, user_class))
    model.add((user, has_email, Literal(user_model.email, datatype=xmls.string)))
    model.add((user, has_password, Literal(user_model.password, datatype=xmls.string)))
    model.add((user, has_location_record, location_record))
    
    # Save the RDF graph to a file
    model.serialize(destination="rdf_files/"+user_model.name+".rdf", format='xml')
    model.close()
    return True


