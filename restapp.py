from fastapi import FastAPI
import data

app = FastAPI()


@app.get("/employee")
async def employee(id: int = 0):
    employees = data.get_employee(id)
    for employee in employees:
        employee['fullName'] = f"{employee['firstName']} {employee['lastName']}"
    return employees


@app.get("/product")
async def product(id: int = 0):
    return data.get_product(id)


@app.get("/supplier")
async def supplier(id: int = 0):
    return data.get_supplier(id)
