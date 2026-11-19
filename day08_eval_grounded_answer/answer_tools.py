from retrieval_tools import search_docs
from model_tools import build_context, build_prompt, call_model
def answer_case(case, docs, model_name):
    # 1. 从 case 中获取问题和关键词
    question = case["question"]
    keywords = case.get("keywords", [])

    # 2. 检索资料
    hits = search_docs(keywords, docs)

    # 3. 构建上下文
    context = build_context(hits)

    # 4. 构建 prompt
    prompt = build_prompt(question, context)

    # 5. 调用模型
    response = call_model(prompt, model_name)

    answer_case ={
        "id": case["id"],
        "question": question,
        "keywords": keywords,
        "sources": [hit["source"] for hit in hits],
        "answer": response.output_text if response else "资料不足，无法确定",
        "status": response.status if response else "error",
        "error": response.error if response and hasattr(response, "error") else None
    }
    # 6. 返回结果
    return answer_case