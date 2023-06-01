from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from Mypacakage import db


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Home Page


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):

    data = db.DB.collection.find({})
    notesData = []
    for i in data:
        # print(i["_id"])
        notesData.append({
            "id": str(i["_id"]),
            "title": i["title"],
            "msg": i["msg"],
        })

    return templates.TemplateResponse("index.html", {"request": request, "notesData": notesData})


@app.post("/")
async def data_insert(request: Request):
    form = await request.form()
    form = dict(form)
    print(form)
    db.DB.collection.insert_one(form)
    data = db.DB.collection.find({})
    notesData = []
    for i in data:
        # print(i["_id"])
        notesData.append({
            "id": str(i["_id"]),
            "title": i["title"],
            "msg": i["msg"],
        })

    return templates.TemplateResponse("index.html", {"request": request, "notesData": notesData})
