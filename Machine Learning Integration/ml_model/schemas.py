from pydantic import BaseModel,Field,StrictInt



class InputSchema(BaseModel):
    longitude:float
    latitude:float#yha par agar input int bhi de denge toh error nhi aayega but once we use strictfloat then sirf input float mein hi valid hoga  
    housian_median_age:int=Field(...,gt=0)#field se validation dete hain(Validation refers to the process of checking whether something meets certain rules, standards, or expectations.)
    total_rooms:StrictInt=Field(...,gt=0)
    total_bedrooms:StrictInt=Field(...,gt=0)
    population:int =Field(...,gt=0)
    households:StrictInt=Field(...,gt=0)
    median_income:float=Field(...,gt=0)

class OutputSchema(BaseModel):
    predicted_price:float



#yah dono housing.csv dataset ke liye define hain jha par input shema wale input lene mein kaam ayenge and the finally the model give the preducted_price as output