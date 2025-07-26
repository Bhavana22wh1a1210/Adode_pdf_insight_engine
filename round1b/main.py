//Persona-Based Relevance Extractor

import os
import json
import datetime
from pdfminer.high_level import extract_text
from sentence_transformers import SentenceTransformer, util

def extract_paragraphs(text):
    return [p.strip() for p in text.split('\n\n') if len(p.strip()) > 40]

def main():
    input_dir = "/app/input"
    output_dir = "/app/output"
    os.makedirs(output_dir, exist_ok=True)

    persona_path = os.path.join(input_dir, "persona.json")
    persona_data = json.load(open(persona_path))
    prompt = f"{persona_data['persona']} - {persona_data['job_to_be_done']}"

    model = SentenceTransformer('all-MiniLM-L6-v2')
    prompt_emb = model.encode(prompt, convert_to_tensor=True)

    result_sections = []
    sub_analysis = []

    for file in os.listdir(input_dir):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(input_dir, file)
            text = extract_text(pdf_path)
            paragraphs = extract_paragraphs(text)

            scores = []
            for i, para in enumerate(paragraphs):
                para_emb = model.encode(para, convert_to_tensor=True)
                sim = util.cos_sim(prompt_emb, para_emb)[0].item()
                scores.append((para, sim, i+1))

            top = sorted(scores, key=lambda x: x[1], reverse=True)[:5]
            for rank, (para, score, idx) in enumerate(top, 1):
                result_sections.append({
                    "document": file,
                    "page": idx,
                    "section_title": para[:60] + "...",
                    "importance_rank": rank
                })
                sub_analysis.append({
                    "document": file,
                    "page": idx,
                    "refined_text": para,
                    "importance_rank": rank
                })

    final_output = {
        "metadata": {
            "documents": [f for f in os.listdir(input_dir) if f.endswith('.pdf')],
            "persona": persona_data["persona"],
            "job_to_be_done": persona_data["job_to_be_done"],
            "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
        },
        "extracted_sections": result_sections,
        "sub_section_analysis": sub_analysis
    }

    with open(os.path.join(output_dir, "result.json"), "w") as out:
        json.dump(final_output, out, indent=2)

if __name__ == "__main__":
    main()
