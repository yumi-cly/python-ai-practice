from model_tools import run_case
from pathlib import Path
import json

# 记得处理“捕获异常＋失败也要保存记录”
def main():
    BASE_DIR = Path(__file__).resolve().parent
    input_path = BASE_DIR / "questions.json"
    with input_path.open("r",encoding="utf-8") as f:
        questions = json.load(f)

    model_name = "gpt-6.1-sol"
    results = []
    completed_count = 0
    failed_count = 0
    total_elapsed_time_ms = 0
    total_count = len(questions)

    for case in questions:
        record = run_case(case, model_name)
        results.append(record)
        total_elapsed_time_ms += record["elapsed_time_ms"]
        if record["status"] == "completed":
            completed_count += 1 
        else:
            failed_count += 1
       
    if total_count > 0:
        average_elapsed_time_ms = total_elapsed_time_ms / total_count
    else:
        average_elapsed_time_ms = None

    summary = {
        "total_count" : total_count,
        "completed_count" : completed_count,
        "failed_count" : failed_count,
        "average_elapsed_time_ms" : average_elapsed_time_ms
    } 

    report = {
        "results": results,
        "summary": summary
    }
    output_path = BASE_DIR / "report.json"
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    
if __name__ == "__main__":
    main()