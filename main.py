from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse
import fitz
import json

app = FastAPI()

@app.post("/generate-pdf/")
async def generate_pdf(data:dict):
    pdf_path = "output.pdf"
    try:
        generate_pdf_from_data(data, pdf_path)
        return FileResponse(pdf_path, filename="generated.pdf")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def generate_pdf_from_data(data, output_path):
    template_path = "templates/template.pdf"
    document = fitz.open(template_path)
    page = document[0]
    page.insert_text((72,72), f"Nombre: {data['name']}", fontsize=12, fontname="helv")
    document.save(output_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)