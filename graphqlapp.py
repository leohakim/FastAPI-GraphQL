from ariadne import ObjectType, QueryType, gql, make_executable_schema
from ariadne.asgi import GraphQL

import data

# Define types using Schema Definition Language (https://graphql.org/learn/schema/)
# Wrapping string in gql function provides validation and better error traceback
type_defs = gql("""
    type Query {
        employee(id: Int): [Employee!]!
        product(id: Int): [Product!]!
        supplier(id: Int): [Supplier!]!
    }
    type Employee {
        id: Int
        firstName: String
        lastName: String
        age: Int
        fullName: String
    }
    type Product {
        id: Int
        name: String
        price: Float
    }
    type Supplier {
        id: Int
        name: String
        address: String
        country: String
        phone: String
    }
""")

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
