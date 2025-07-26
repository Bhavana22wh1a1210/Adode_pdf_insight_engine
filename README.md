# 📘 Adobe Hackathon - Round 1B

## 🧠 Problem Statement
Build a persona-based intelligent system to extract and rank the most relevant sections from multiple PDFs based on:
- A given persona
- A job-to-be-done (goal/task)

### 🧾 Output Format (result.json)
```json
{
  "metadata": {
    "documents": ["sample.pdf"],
    "persona": "...",
    "job_to_be_done": "...",
    "timestamp": "..."
  },
  "extracted_sections": [...],
  "sub_section_analysis": [...]
}
```

---

## 📁 Project Structure
```
round1b/
├── main.py
input/
├── sample.pdf
├── persona.json
output/
├── result.json
Dockerfile
requirements.txt
README.md
approach_explanation.md
```

---

## 🐳 Docker Instructions

### ✅ Build the Docker Image
```bash
docker build --platform linux/amd64 -t adobe-persona-extractor .
```

### ▶️ Run the Container
```bash
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none adobe-persona-extractor
```

---

## 🧰 Dependencies
- `pdfminer.six`
- `sentence-transformers`
- `torch`, `numpy`, `scikit-learn`

All installed via `requirements.txt` during build.

---

## ⚠️ Constraints Met
- ✅ Runtime ≤ 60s for 3–5 PDFs
- ✅ Model size ≤ 1GB (`all-MiniLM-L6-v2` ~90MB)
- ✅ CPU-only, AMD64-compatible
- ✅ No internet/network access

---

## 📌 Notes
- Paragraphs ranked using semantic similarity with persona + task embedding
- Output is structured and sorted by relevance score
