import json
from pathlib import Path 
from case_tools import evaluate_case,summarize

def main():
    base_dir = Path(__file__).resolve().parent
    input_path = base_dir / "tests.json"
    output_path = base_dir / "results.json"
    threshold_ms = 2000
    #处理异常
    try:
        with input_path.open("r", encoding="utf-8") as f:
            test_cases = json.load(f)
    except FileNotFoundError:
        print(f"输入文件不存在：{input_path}")
        return
    except json.JSONDecodeError as error:
        print(f"JSON格式错误：第{error.lineno}行第{error.colno}列")
        return

    results = []
    for case in test_cases:
        result = evaluate_case(case,threshold_ms)
        results.append(result)
    summary = summarize(results)
    report = {
        "threshold_ms":threshold_ms,
        "results":results,
        "summary":summary
    }
    with output_path.open("w",encoding="utf-8") as f:
        json.dump(report,f,ensure_ascii=False,indent=2)
    print(summary)

if __name__=="__main__":
    main()
    