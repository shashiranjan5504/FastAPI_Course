import models,schemas,crud
from fastapi import FastAPI,HTTPException,Depends
from sqlalchemy.orm import Session
from database import engine,sessionlocal,Base
from typing import List

Base.metadata.create_all(bind=engine)
app=FastAPI()

# dependecy with the db
def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close() 

#creating endpoints
#1.create an employee
@app.post("/employees",response_model=schemas.EmployeeOut)
def create_employee(new_employee:schemas.EmployeeCreate,db:Session=Depends(get_db)):
    return crud.create_employee(db ,new_employee)
#2.get all employees
@app.get("/employees",response_model=List[schemas.EmployeeOut])
def get_all_employees(db:Session=Depends(get_db)):
    return crud.get_employees(db)
#3.get employee specifically
@app.get("/employees/{emp_id}",response_model=schemas.EmployeeOut)
def get_employee(emp_id:int,db:Session=Depends(get_db)):
    employee=crud.get_employee(db,emp_id)
    if  employee:
        return employee
    else:
        raise HTTPException(status_code=404,detail="Employee Not Found")
    
#4.update an employee
@app.put("/employees/{emp_id}",response_model=schemas.EmployeeOut)
def update_employee(emp_id:int,new_employee:schemas.EmployeeUpdate,db:Session=Depends(get_db)):
    employee=crud.update_employee(db,emp_id,new_employee)
    if employee is None:
        raise HTTPException(status_code=404,detail="Employee Not Found")
    return employee
    
#5.delete an employee
@app.delete("/employees/{emp_id}", response_model=dict)
def delete_employee(emp_id:int,db:Session=Depends(get_db)):
    employee=crud.delete_employee(db,emp_id)
    if employee is None:
        raise HTTPException(status_code=404,detail="Employee Not Found")
    return {'detail':"Delete Successfully"}

