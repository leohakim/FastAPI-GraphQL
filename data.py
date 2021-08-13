employee_data = [
    {"id": 1001, "firstName": "John", "lastName": "Doe", "age": 28},
    {"id": 1002, "firstName": "Bob", "lastName": "McBobby", "age": 45},
]

product_data = [
    {"id": 2011, "name": "Tofu", "price": 12.7},
    {"id": 2012, "name": "Chocolate", "price": 18.2},
    {"id": 2013, "name": "Pepper Sauce", "price": 23.3},
]

supplier_data = [
    {"id": 4101, "name": "Tokyo Sweet", "address": "7-11 Akimai Mushi-shi", "country": "Japan", "phone": "(03) 3555-5011 "},
    {"id": 4102, "name": "New England", "address": "85 King's Street", "country": "United Kingdom", "phone": "(171) 555-2222 "},
]


def get_employee(id):
    if id:
        return [x for x in employee_data if x['id'] == id]

    return employee_data


def get_product(id):
    if id:
        return [x for x in product_data if x['id'] == id]

    return product_data


def get_supplier(id):
    if id:
        return [x for x in supplier_data if x['id'] == id]

    return supplier_data
