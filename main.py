from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/Welcome")
def Welcome():
    return {"message": "Welcome to Fast API!"}
    