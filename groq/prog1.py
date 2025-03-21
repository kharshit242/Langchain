from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

model = init_chat_model("llama3-8b-8192", model_provider="groq")

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)
