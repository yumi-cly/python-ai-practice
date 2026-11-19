from eval_tools import evaluate_record
from answer_tools import answer_case
from retrieval_tools import load_docs
import json
from pathlib import Path

def main():
    results = []
    base_dir = Path(__file__).resolve().parent
    input_path = base_dir / "questions.json"
    docs_dir = base_dir / "docs"
    docs = load_docs(docs_dir)

    with input_path.open("r", encoding="utf-8") as f:
        questions = json.load(f)

    model_name = "gpt-6.1-sol"  

    for case in questions:
        record = answer_case(case, docs, model_name)
        evaluation = evaluate_record(record, case["expected"])
        results.append({"record": record, "evaluation": evaluation})

    # 统计并保存
    total = len(results)
    passed_count = 0
    for item in results:
        if item["evaluation"]["passed"]:
            passed_count += 1
    pass_rate = passed_count / total  if total > 0 else 0
    summary = {
        "total": total,
        "passed": passed_count,
        "not_passed": total - passed_count,
        "rule_pass_rate": pass_rate}
    report = {
        "summary": summary,"results": results
    }

    # 输出报告

    output_path = base_dir / "eval_report.json"
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()