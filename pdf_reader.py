import fitz #PyMuPDF se importa con el nombre fitz

def extraer_texto (archivo_pdf):
    documento = fitz.open(stream=archivo_pdf.read(), filetype="pdf")
    texto= ""
    for pagina in documento:
        texto += pagina.get_text()
    return texto 