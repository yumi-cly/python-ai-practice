# 调用模型并返回运行记录
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

def call_model(question):
    # Microsoft Entra ID authentication (recommended)
    # This automatically uses environment variables, managed identity, or Azure CLI credentials
    token_provider = get_bearer_token_provider(
        DefaultAzureCredential(),"https://ai.azure.com/.default"
    )

    client = OpenAI(
        base_url="https://foundry-yumi.openai.azure.com/openai/v1/",
        api_key=token_provider(),
        timeout=2.0,     # 超时 2000 毫秒(单位是秒)
        max_retries=0,   # openai 客户端默认超时/连接失败会自动重试 2 次,不关掉的话实际要等 3 轮超时才抛异常,设为 0 才能让超时立刻生效
    )

    response = client.responses.create(
        model="gpt-6.1-s",
        input=question
    )

    return response



