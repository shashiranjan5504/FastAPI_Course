from fastapi import FastAPI,HTTPException
from models_val import Employee
from typing import List



employees_db:List[Employee]=[]
app=FastAPI()
#1. reading all employees
@app.get("/employees",response_model=List[Employee])
def get_all_employees():
    return employees_db

#2.reading employee specifically
@app.get("/employees/{emp_id}",response_model=Employee)
def get_employee_by_id(emp_id:int):
    for index,employee in enumerate(employees_db):
        if employee.id==emp_id:
            return employee
    raise HTTPException(status_code=404,detail="Employee not Found")
        
#3.adding a employee
@app.post("/add_employee")
def add_employee(new_emp:Employee):
    for employee in employees_db:
        if employee.id==new_emp.id:
            raise HTTPException(status_code=400,detail="employee already exists")
    employees_db.append(new_emp)
    return new_emp

#4. updating a employee
@app.put("/update_employee/{emp_id}")
def update_employee(emp_id:int,new_emp:Employee):
    for index,employee in enumerate(employees_db):
        if employee.id==emp_id:
            # employee=new_emp   yeh galat hai actually employee is just a tagger it  does not change  the value
            employees_db[index]=new_emp 
            return employees_db[index]#now it actually return the updated value .there  is still one more method that is in the video
    raise HTTPException( status_code=404,detail="Employee Not Found")

#5.deleting an employee
@app.delete("/delete_employee/{emp_id}")
def delete_employee(emp_id:int):
    for index,employee in enumerate(employees_db):
        if employee.id==emp_id:
            del  employees_db[index]
            return {'message':'Employee deleted successfully'}
    raise HTTPException(status_code=404,detail="Employee Not Found")            
        
    


