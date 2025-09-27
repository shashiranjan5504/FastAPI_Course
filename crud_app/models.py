from sqlalchemy import column,Integer,String
from database import Base


class Employee(Base):
    __tablename__="employees"
    id=column(Integer,primary_key=True,index=True)
    name=column(String,index=True)
    email=column(String,unique=True,index=True)
    #index=for faster retrieval \
    #classs emplyeee ka schemsa define ho rha hai 
