from model_tools import call_model
from pathlib import Path
import json
import time
import openai

# 记得处理“捕获异常＋失败也要保存记录”
def main():

    start = time.perf_counter() #调用前记录时间
    question = "JSON文件与Python字典有什么区别"

    response = None
    error_message = None
    try:
        response = call_model(question)
    except openai.APITimeoutError as e:
        error_message = f"OpenAI API request timed out (>2000ms): {e}"
    except openai.APIConnectionError as e:
        error_message = f"Failed to connect to OpenAI API: {e}"
    except openai.RateLimitError as e:
        error_message = f"OpenAI API request exceeded rate limit: {e}"
    except openai.APIError as e:
        error_message = f"OpenAI API returned an API Error: {e}"

    end = time.perf_counter() #调用后记录时间

    elapsed_time = (end - start) * 1000  # 转换为毫秒

    if response is not None:
        record = {
            "question": question,
            "model": response.model,
            "answer": response.output_text,
            "elapsed_time_ms": elapsed_time,
            "status": response.status,
            "error": error_message,
        }
    else:
        record = {
            "question": question,
            "model": None,
            "answer": None,
            "elapsed_time_ms": elapsed_time,
            "status": "failed",
            "error": error_message,
        }

    BASE_DIR = Path(__file__).resolve().parent
    output_path = BASE_DIR / "answer.json"
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(record, f, ensure_ascii=False, indent=2)

    if record["status"] == "completed":
        print(f"Model call completed successfully. Call model took {elapsed_time:.2f} milliseconds. Answer saved to {output_path}.")
    else:
        print(f"Model call failed with status: {record['status']}")
        print(f"Error details: {record['error']},Call model took {elapsed_time:.2f} milliseconds, Answer is none.")
    
if __name__ == "__main__":
    main()