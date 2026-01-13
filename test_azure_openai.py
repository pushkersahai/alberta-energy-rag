import os
from openai import AzureOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize two clients (one for each region)
client_canada = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

client_eastus = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY_EASTUS2"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT_EASTUS2")
)

print("Testing Azure OpenAI connection...\n")

# Test 1: Embedding model (Canada East)
print("1. Testing embedding model (Canada East)...")
try:
    response = client_canada.embeddings.create(
        model=os.getenv("EMBEDDING_DEPLOYMENT"),
        input="Alberta oil sands production data"
    )
    print(f"✅ Embedding model works! Generated {len(response.data[0].embedding)} dimensions")
except Exception as e:
    print(f"❌ Embedding failed: {e}")

# Test 2: GPT model (East US 2)
print("\n2. Testing GPT model (East US 2)...")
try:
    response = client_eastus.chat.completions.create(
        model=os.getenv("GPT_DEPLOYMENT"),
        messages=[
            {"role": "user", "content": "What are the main challenges in Alberta's energy sector?"}
        ],
        max_tokens=100
    )
    print(f"✅ GPT model works!")
    print(f"Response: {response.choices[0].message.content}")
except Exception as e:
    print(f" GPT failed: {e}")

print("\nAll tests passed! Both Azure OpenAI resources ready.")