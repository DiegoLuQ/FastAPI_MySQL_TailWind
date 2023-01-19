from pydantic import BaseModel

def ReponseModel(code,message,data):
    return {
        "code":code,
        "message":message,
        "data":data
    }