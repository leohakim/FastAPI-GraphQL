from ariadne import ObjectType, QueryType, gql, make_executable_schema, load_schema_from_path
from ariadne.asgi import GraphQL

import data

type_defs = load_schema_from_path("schema.graphql")

# Map resolver functions to Query fields using QueryType
query = QueryType()


# Resolvers are simple python functions
@query.field("employee")
def resolve_employee(_, info, id=0):
    return data.get_employee(id)


@query.field("product")
def resolve_product(_, info, id=0):
    return data.get_product(id)


@query.field("supplier")
def resolve_supplier(_, info, id=0):
    return data.get_supplier(id)


# Map resolver functions to custom type fields using ObjectType
employee = ObjectType("Employee")


@employee.field("fullName")
def resolve_person_fullname(person, *_):
    return "%s %s" % (person["firstName"], person["lastName"])


# Create executable GraphQL schema
schema = make_executable_schema(type_defs, query, employee)

# Create an ASGI app using the schema, running in debug mode
app = GraphQL(schema, debug=True)
