
# Approach Explanation 

## 🧠 Round 1B – Persona-Based Document Intelligence

### Objective
To extract and rank the most relevant sections from multiple PDFs, based on a given persona and a job-to-be-done task.

### Methodology
We designed a modular pipeline using semantic similarity to find sections aligned with user intent.

#### 1. **Input Parsing**
- Multiple PDFs are processed using `pdfminer.six`
- Each document is segmented into paragraphs for evaluation

#### 2. **Prompt Embedding**
- The combined **persona** and **job** are encoded using `sentence-transformers` (`all-MiniLM-L6-v2`)
- This forms the context embedding to compare with document sections

#### 3. **Semantic Matching**
- Each paragraph is embedded and scored using cosine similarity against the prompt
- Top 5 most relevant sections per document are extracted and ranked

#### 4. **Output**
- Structured JSON with metadata, top extracted sections, and sub-section analyses (with rank, page number, and refined content)

### Model & Constraints
- Used `all-MiniLM-L6-v2` (model size < 90MB)
- Fully offline, CPU-compatible, and efficient (≤ 60 seconds for 5 PDFs)

---

## 🔐 Compliance with Constraints

| Constraint                | Status |
|---------------------------|--------|
| Model size ≤ 1GB          | ✅ ~90MB (MiniLM) |
| Runtime ≤ 60 seconds      | ✅ Tested with 3–5 PDFs |
| CPU-only                  | ✅ No GPU usage |
| No internet/network usage | ✅ Handled via Docker `--network none` |
| Docker-compatible         | ✅ Works with AMD64 base image |

---

## 📌 Design Considerations
- Modular code structure to reuse PDF parsing logic between rounds
- Dockerized for consistent local and remote execution
- Built for generalization — not hardcoded to any specific document layout

---

## 💡 Future Enhancements (For Round 2/3)
- Contextual linking of ideas across documents
- More robust section splitting using layout analysis
- Fine-grained entity extraction for deeper insight


