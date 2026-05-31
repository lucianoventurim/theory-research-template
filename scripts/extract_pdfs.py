from pathlib import Path
import fitz  # PyMuPDF

ROOT = Path(__file__).resolve().parents[1]
PDF_DIR = ROOT / "literature" / "pdfs"
OUT_DIR = ROOT / "literature" / "extracted-text"

OUT_DIR.mkdir(parents=True, exist_ok=True)

def extract_pdf(pdf_path: Path) -> str:
    parts = []
    with fitz.open(pdf_path) as doc:
        for page_num, page in enumerate(doc, start=1):
            text = page.get_text()
            parts.append(f"\n\n--- Page {page_num} ---\n\n{text}")
    return "".join(parts)

def main():
    pdfs = sorted(PDF_DIR.glob("*.pdf"))
    if not pdfs:
        print(f"No PDFs found in {PDF_DIR}")
        return

    for pdf in pdfs:
        out = OUT_DIR / f"{pdf.stem}.txt"
        print(f"Extracting {pdf.name} -> {out.name}")
        text = extract_pdf(pdf)
        out.write_text(text, encoding="utf-8")

if __name__ == "__main__":
    main()