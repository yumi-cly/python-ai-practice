from langchain_core.documents import Document

document = Document(
    page_content="产品A保修12个月。人为损坏不在保修范围。",
    metadata={"source": "02_warranty.txt"}
)
 
print(type(document).__name__)
print(document.page_content)
print(document.metadata)
print(document.metadata["source"])