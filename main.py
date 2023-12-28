from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from imap2dict import MailClient

app = FastAPI()

class FetchMailRequest(BaseModel):
    host_name: str
    user_id: str
    password: str
    search_option: str = "UNSEEN"
    timezone: str = "Asia/Tokyo"

class DeleteMailRequest(BaseModel):
    host_name: str
    user_id: str
    password: str
    days: int = 90

@app.post("/fetch_mail")
def fetch_mail(request: FetchMailRequest):
    cli = MailClient(request.host_name, request.user_id, request.password)
    messages = cli.fetch_mail(search_option=request.search_option, timezone=request.timezone)
    return {"status": "OK", "messages": messages}

@app.delete("/delete_mail")
def delete_mail(request: DeleteMailRequest):
    cli = MailClient(request.host_name, request.user_id, request.password)
    delete_count = cli.delete_mail(days=request.days)
    return {"delete_count": delete_count}
