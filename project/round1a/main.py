import os
import json
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

def extract_outline_from_pdf(pdf_path):
    headings = []
    title = os.path.splitext(os.path.basename(pdf_path))[0]
    for page_number, layout in enumerate(extract_pages(pdf_path), start=1):
        for element in layout:
            if isinstance(element, LTTextContainer):
                text = element.get_text().strip()
                if text.isupper() and len(text.split()) <= 10:
                    headings.append({"level": "H1", "text": text, "page": page_number})
                elif len(text.split()) <= 8 and text.istitle():
                    headings.append({"level": "H2", "text": text, "page": page_number})
                elif len(text.split()) <= 6:
                    headings.append({"level": "H3", "text": text, "page": page_number})
    return {
        "title": title,
        "outline": headings
    }

def main():
    input_dir = "/app/input"
    output_dir = "/app/output"
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            result = extract_outline_from_pdf(pdf_path)
            json_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.json")
            with open(json_path, "w") as f:
                json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
