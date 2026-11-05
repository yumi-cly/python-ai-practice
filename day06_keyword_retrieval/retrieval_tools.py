def load_docs(docs_dir):
    docs = []
    # 找到文件夹里的所有 .txt 文件，按文件名排序，再逐个处理
    for path in sorted(docs_dir.glob("*.txt")):
        # 读取当前文件的内容，存到字符串 text 中
        text = path.read_text(encoding="utf-8")
        docs.append({"source": path.name, "text": text})
    return docs

def search_docs(keywords, docs):
    hits = []

    if keywords is not None and len(keywords) > 0:
        for doc in docs:
            matched_keywords = []

            for keyword in keywords:
                if keyword and keyword in doc["text"]:
                    matched_keywords.append(keyword)

            # 检查完这份资料的所有关键词，再决定是否加入
            if matched_keywords:
                hits.append({
                    "source": doc["source"],
                    "text": doc["text"],
                    "matched_keywords": matched_keywords
                })
    return hits
