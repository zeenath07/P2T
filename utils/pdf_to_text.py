import pdfplumber
from typing import BinaryIO

def pdf_to_text(file_obj: BinaryIO) -> str:
    """
    Accepts a file-like object (bytes stream) and returns extracted text.
    Uses pdfplumber to better handle layout/characters.
    """
    all_text = []
    with pdfplumber.open(file_obj) as pdf:
        for page in pdf.pages:
            # you can use page.dedupe_chars() if you see duplicated chars in some PDFs
            try:
                # prefer dedupe + extract_text for robustness:
                text = page.dedupe_chars().extract_text() or ""
            except Exception:
                text = page.extract_text() or ""
            all_text.append(text)
    return "\n\n".join(all_text)
