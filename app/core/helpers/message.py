from pydantic import BaseModel

def ReponseModel(code,message,data):
    return {
        "code":200,
        "message":message,
        "data":data
    }