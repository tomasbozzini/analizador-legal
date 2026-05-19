# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the App

```bash
# Activate virtual environment (Windows)
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app runs on `http://localhost:8501` by default.

## Environment

Requires a `.env` file in the project root with:
```
GEMINI_API_KEY=your_key_here
```

## Architecture

Single-purpose pipeline: PDF upload → text extraction → Gemini analysis → Markdown output.

```
app.py (Streamlit UI)
  ├── pdf_reader.py   — extraer_texto(archivo_pdf): reads PDF bytes via PyMuPDF, returns plain text
  ├── analyzer.py     — analizar_documento(texto): sends text to Gemini, returns analysis string
  └── prompts.py      — SISTEMA: system prompt defining output format (summary, clauses, questions)
```

**Key details:**
- Model: `gemini-2.0-flash` configured with `system_instruction=SISTEMA`
- PDF parsing: PyMuPDF (`fitz`), opened from bytes stream
- Output rendered as Markdown in Streamlit
- All user-facing text and code comments are in Spanish

## No Tests or Linting

There is no test suite or linter configured for this project.
