from fastapi import FastAPI,status
from schemas import EmailRequest,EmailResponse
import uvicorn
app = FastAPI()

@app.post("/email",response_model=EmailResponse,status_code=status.HTTP_200_OK)
async def send_email(email_request: EmailRequest):
    return EmailResponse(message="Email Send", success=True)



if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8020)