from typing import Union
from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "FastAPI"}
@app.get("/page/{id}")
def get_page(id):
    return {"data":f"Page的ID是：{id}"}
@app.get("/articles/all")
def get_blogs_all(page, page_size):
    return {"message": f"所有的 articles： 來自第 {page} 頁， 總共有 {page_size} 筆資料"}
