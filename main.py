from model import mode_pipeline
from fastapi import FastAPI, UploadFile
import io
from PIL import Image

app = FastAPI()

@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.post('/ask')
def ask(text: str, image: UploadFile):
    content = image.file.read()
    
    image = Image.open(io.BytesIO(content))
    #image = Image(image.file)
    result = mode_pipeline(text, image)

    return {"answer" : result}
