from pathlib import Path
from document_tools import load_documents, split_documents

base_dir = Path(__file__).resolve().parent
documents = load_documents(base_dir / "docs")

for size, overlap in [(500,50),(20,4),(40,4),(20,0)]:
    chunks = split_documents(documents, size, overlap)
    print("参数", size, overlap, "片段数", len(chunks))
    for chunk in chunks:
        print(chunk.metadata, len(chunk.page_content))
   
   