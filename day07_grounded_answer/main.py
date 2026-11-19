#配置路径和输入 → 读取资料 → 检索 → 初始化记录 → 判断是否命中 → 拼上下文与提示词 → 调用模型 → 更新记录 → 保存JSON

from retrieval_tools import load_docs, search_docs
from model_tools import call_model,run_case,build_context,build_prompt
import json
from pathlib import Path

def main():
    question = "保修是否包含上门维修？"
    keywords = ["保修"]
    base_dir = Path(__file__).resolve().parent
    docs_dir = base_dir / "docs"
    docs = load_docs(docs_dir)
    hits = search_docs(keywords, docs)
    sources = [hit["source"] for hit in hits]
    # 遍历 hits，取出每份资料的 "source"，放进新列表 sources
    # sources = []
    # for hit in hits:
    #    sources.append(hit["source"])
        
    record = {
        "question": question, "keywords": keywords,
        "sources": sources, "answer": None,
        "status": "no_hit", "error": None
    }

    if not hits:
        print("未找到匹配资料。")
    else:
        context = build_context(hits)
        prompt = build_prompt(question, context)
        # 把完整提示词交给模型，而不只是原始问题
        case = {
            "id": "Q001",
            "question": prompt
        }

        result = run_case(
            case,
            model_name="gpt-6.1-sol"  # 使用你之前成功调用的部署名
        )

        # 把调用结果填进本次记录
        record["answer"] = result["answer"]
        record["status"] = result["status"]
        record["error"] = result["error"]

        print("回答：", record["answer"])
        print("状态：", record["status"])
        print("错误：", record["error"])
    output_path = base_dir / "answer_results.json"
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()