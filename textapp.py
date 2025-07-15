import dotenv
import os
dotenv.load_dotenv()
from openai import AzureOpenAI



endpoint = "https://newazuredeployment.openai.azure.com/"
model_name = "o3-mini"
deployment = "o3-mini"

subscription_key = os.getenv("AZURE_OPENAI_KEY")

api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "I am going to Paris, what should I see?",
        }
    ],
    max_completion_tokens=100000,
    model=deployment
)

print(response.choices[0].message.content)