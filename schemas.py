from pydantic import BaseModel,EmailStr
class EmailRequest(BaseModel):
    email: EmailStr



class EmailResponse(BaseModel):
    message: str
    success: bool