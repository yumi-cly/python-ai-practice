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
        model = model_name,
        input = question
    )

    return response


def build_context(hits):
    parts = []
    for hit in hits:
        source = hit["source"]
        text = hit["text"]
        part = f"资料来源：{source}\n内容：{text}"
        parts.append(part)
    return "\n\n".join(parts) #\n表示换行；"\n\n".join(parts)用两个换行连接各段

def build_prompt(question, context):
    prompt = f"""请仅依据提供的资料回答问题。
资料不足时明确回答“资料不足，无法确定”。
请在答案中标注支持结论的来源文件名。
不要使用资料之外的信息补充事实。

【资料开始】
{context}
【资料结束】

问题：{question}"""

    return prompt