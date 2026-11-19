def evaluate_record(record, expected):
    #首先要明确record和expected的输入输出
    reasons = []

    # 1. 检查状态
    if record["status"] != expected["status"]:
        reasons.append(
            f"状态不符：预期{expected['status']}，实际{record['status']}"
        )
    # 2. 检查来源，忽略文件顺序，可以用 set() 来忽略顺序和重复值
    if set(record["sources"]) != set(expected["sources"]):
        reasons.append("检索来源不符")
        
    # 3. 没有命中时，不应该留下答案或来源
    if record["status"] == "no_hit":
        if record["answer"] is not None or record["sources"] != []:
            reasons.append("无命中时，答案应为None，来源应为空列表")
    
    # 4.调用完成时，检查回答
    if record["status"] == "completed":
        answer = record["answer"]

        if not isinstance(answer, str) or not answer.strip():
            reasons.append("回答为空或不是字符串")
        else:
            for item in expected["required_terms"]:
                if item not in answer:
                    reasons.append(f"回答不包含预期内容：{item}")

    # 所有检查结束后，再返回结果
    return {
        "passed": len(reasons) == 0,
        "reasons": reasons
    }