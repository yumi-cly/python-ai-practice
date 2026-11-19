from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_documents(docs_dir):
    documents = []
    for path in sorted(docs_dir.glob("*.txt")):
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            continue
        document = Document(
            page_content=text,
            metadata={"source": path.name}
        )
        documents.append(document)
    return documents

def split_documents(documents, chunk_size=20, chunk_overlap=4):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        separators=["\n\n", "\n", "。", "，", " ", ""],
        add_start_index=True
    )
    return splitter.split_documents(documents)


