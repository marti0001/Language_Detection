from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, constr
from sklearn.preprocessing import LabelEncoder
import numpy as np
import io
import os
import joblib

script_dir = os.path.dirname(__file__)
model_path = os.path.join(script_dir,'model','Pipeline_and_model_Language_Detection-0.1.0.pkl')
templates_dir = os.path.join(script_dir,'templates')

# ładowanie modelu
try:
    model = joblib.load(model_path)
except Exception as e:
    print(f"bład podczas ładowania modelu: {e}")

app = FastAPI()
templates = Jinja2Templates(directory= templates_dir)

#model danych wejsciowych
class TextInput(BaseModel):
    text: constr(min_length=1, max_length=1000)  # tekst 1-1000 znaków
    @classmethod
    def as_form(cls,text: str = Form(...)):
        return cls(text= text)
        

#strona główna renderowanie 
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request}) 


@app.post("/predict")
async def predict(request: Request, input_data: TextInput  = Depends(TextInput.as_form)):
    try:
        # Poprawione: użyj input_data.text i konwersja na listę
        text_to_predict = [input_data.text]
        
        # Wykonaj predykcję
        prediction = model.predict(text_to_predict)[0]

        LANGUAGE_MAP = {
            0: 'Danish',
            1: 'Dutch',
            2: 'English',
            3: 'Finnish',
            4: 'French',
            5: 'German',
            6: 'Italian',
            7: 'Norwegian',
            8: 'Polish',
            9: 'Portuguese',
            10: 'Russian',
            11: 'Swedish',
            12: 'Spanish',
            13: 'Ukrainian',
            }
        language_name = LANGUAGE_MAP.get(prediction, 'Nieznany język')
        
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "prediction": language_name,
                "original_text": input_data.text  # Poprawione: przekaż tekst
            }
        )
    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "error": f"Błąd predykcji: {str(e)}",
                "original_text": input_data.text if input_data else ""
            }
        )

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)


