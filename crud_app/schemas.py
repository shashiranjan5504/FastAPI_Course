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


        #jo bho cpmmon fields hai usko basde model mein define kr denge but jo specifuc hainusk alg se define kr sajye ahin 
#name and email are only required to creat an emolpyee as id is auto dgenerated 