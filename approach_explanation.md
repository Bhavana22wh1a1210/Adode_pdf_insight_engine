
```md
# Approach Explanation

## Round 1A
We used `pdfminer.six` to parse the document layout. Headings are identified by analyzing the font style, text case, and layout positioning heuristically. The goal is to build a generalizable extractor that avoids hardcoded values.

## Round 1B
We implemented a relevance scorer using `sentence-transformers` to compare paragraph embeddings against the persona + job prompt. Sections with the highest cosine similarity are considered most relevant.

- The model `all-MiniLM-L6-v2` is under 90MB, fast, and works offline.
- Paragraphs are ranked and returned along with metadata.

Both modules are CPU-only, run within the required time constraints, and are packaged for AMD64 architecture.
