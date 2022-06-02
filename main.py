# from typing import Union
#
# import uvicorn as uvicorn
# from fastapi import FastAPI
#
# app = FastAPI()
#
#
# @app.get("/")
# def read_root():
#     return {"first_name": "Jyotsna"}
#
#
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
#
#
# @app.get("/auth")
# def read_item(api_key: Union[str, None] = None):
#     if api_key == '1234':
#         return {'status': 'OK'}, 200
#     return {'status':''}, 210
#
#
# if __name__ == "__main__":
#     uvicorn.run("example:app", host="127.0.0.1", port=5000, log_level="info")
#

def foo():
    return {'hello':'bye'}