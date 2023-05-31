from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from Mypacakage import db

# client = p.MongoClient("mongodb+srv://suvenduc789:suvenduc789@cluster0.5hfi8pd.mongodb.net/?retryWrites=true&w=majority")
# db = client['Notes']
# collection = db['mynotes']

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Home Page
@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):

    data = db.DB.collection.find({})
    for i in data:
        print(i["msg"])
    return templates.TemplateResponse("index.html", {"request": request})
