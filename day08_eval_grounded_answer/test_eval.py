from eval_tools import evaluate_record

# 预期结果，作为检查标准
expected = {
      "status": "completed",
      "sources": ["02_warranty.txt"],
      "required_terms": ["12个月", "人为损坏"]
}

# 模拟模型返回的实际结果
record = {
    "id": "Q001",
    "status": "completed",
    "sources": ["02_warranty.txt"],
    "answer": None,
    "error": None
}
record["answer"] = "保修12个月，人为损坏也保修。"
result = evaluate_record(record, expected)
print(result)

#返回结果{'passed': True, 'reasons': []}
#介入人工判断：答案错误。02_warranty.txt写着“人为损坏不在保修范围”，模拟答案却说“也保修”。
#说明检查看到了关键词，却没有进行语义判断。