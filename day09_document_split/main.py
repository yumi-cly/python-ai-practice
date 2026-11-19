import json
from pathlib import Path
from document_tools import load_documents, split_documents

def main():
    base_dir = Path(__file__).resolve().parent
    documents = load_documents(base_dir/"docs")
    chunks = split_documents(documents, chunk_size=20, chunk_overlap=4)
    results = []

    for index, chunk in enumerate(chunks,start=1):
        results.append({
            "chunk_id" : index,
            "page_content" : chunk.page_content,
            "metadata" : chunk.metadata
        })
        print(index,chunk.metadata, len(chunk.page_content))
        print(chunk.page_content)

    report = {
        "document_count" : len(documents),
        "chunk_count" : len(chunks),
        "chunks_size" : 20,
        "chunks_overlap" : 4,
        "chunks" : results
    }
    with (base_dir / "chunks.json").open("w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
 
if __name__ == "__main__":
    main()

