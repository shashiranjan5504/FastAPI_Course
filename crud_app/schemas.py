from pydantic import BaseModel,EmailStr


class EmployeeBase(BaseModel):
    name :str
    email:EmailStr

class EmployeeCreate(EmployeeBase):#for creation
    pass


class EmployeeUpdate(EmployeeBase):#for updation 
    pass 

class EmployeeOut(EmployeeBase):#data is  being sent 
    id:int


    class Config:
        orm_mode=True


        #jo bho common fields hai usko employeebase mein define kr denge but jo specifuc hain usko alag se define kr sakte hain 
#name and email are only required to creat an emolpyee as id is auto generated 