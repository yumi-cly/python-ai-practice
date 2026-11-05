# 调用模型并返回运行记录
import time

from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider
from azure.core.exceptions import ClientAuthenticationError
import openai

def call_model(question,model_name, timeout_seconds=30.0):
    # Microsoft Entra ID authentication (recommended)
    # This automatically uses environment variables, managed identity, or Azure CLI credentials
    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(),"https://ai.azure.com/.default"
    )

    client = OpenAI(
        base_url="https://foundry-yumi.openai.azure.com/openai/v1/",
        api_key=token_provider(),
        timeout=timeout_seconds,     # 单位是秒
        max_retries=0,   # openai 客户端默认超时/连接失败会自动重试 2 次,不关掉的话实际要等 3 轮超时才抛异常,设为 0 才能让超时立刻生效
    )

    response = client.responses.create(
        model=model_name,
        input=question
    )

    return response

def run_case(case, model_name):
    start_time = time.perf_counter()
    answer = None 
    # 如果 call_model() 报错，下面的 answer = ... 就不会执行。但最后返回记录时，仍然需要使用 answer
    status = "failed"
    error_message = None

    try:
        response = call_model(case["question"], model_name=model_name)
        answer = response.output_text
        status = response.status

        if response.error is not None:
            error_message = str(response.error)
        elif status != "completed":
            error_message = "响应未完成"

    except openai.APITimeoutError as error:
        error_message = f"请求超时：{error}"

    except openai.APIError as error:
        error_message = f"接口调用失败：{error}"

    except ClientAuthenticationError as error:
        error_message = f"Entra认证失败：{error}"


    end_time = time.perf_counter()
    elapsed_time = (end_time - start_time) * 1000

    record = {
        "id": case["id"],
        "question": case["question"],
        "requested_model": model_name,
        "answer": answer,
        "elapsed_time_ms": elapsed_time,  # 转换为毫秒
        "status": status,
        "error": error_message
    }

    return record