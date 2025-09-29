from sqlalchemy.orm import Session
import models,schemas

def get_employees(db:Session):#jitne bhi operation hoga woh session mein  hoga so we ac
    return db.query(models.Employee).all()

def get_employee(db:Session,emp_id:int):
    return(
        db
        .query(models.Employee)
        .filter(models.Employee.id==emp_id)#check kr rhr hai 
        .first()#pahela wala match return kr denge 
    )
def create_employee(db:Session,new_employee:schemas.EmployeeCreate):
    db_employee=models.Employee(
        name=new_employee.name,email=new_employee.email
        )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee
def update_employee(db:Session,emp_id:int,new_employee:schemas.EmployeeUpdate):
    db_employee=db.query(models.Employee).filter(models.Employee.id==emp_id).first()
    if db_employee:
        db_employee.name=new_employee.name
        db_employee.email=new_employee.email
        db.commit()
        db.refresh(db_employee)
    return db_employee
def delete_employee(db:Session,emp_id:int):
    db_employee=db.query(models.Employee).filter(models.Employee.id==emp_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee

        

       
