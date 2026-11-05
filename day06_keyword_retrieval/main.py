from pathlib import Path
from retrieval_tools import load_docs, search_docs
import json

base_dir = Path(__file__).resolve().parent
docs_dir = base_dir / "docs"
docs = load_docs(docs_dir)
keywords = ["保修", "人为损坏"]
hits = search_docs(keywords, docs)
report = {"keywords": keywords, "results": hits}
# 无论有没有命中，都保存本次结果
output_path = base_dir / "retrieval_results.json"
with output_path.open("w", encoding="utf-8") as f:
    json.dump(report, f, ensure_ascii=False, indent=2)
if not hits:
    print("未找到匹配资料。")