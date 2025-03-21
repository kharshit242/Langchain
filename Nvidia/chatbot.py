from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

model=init_chat_model("nvidia/llama-3.3-nemotron-super-49b-v1", model_provider="nvidia")

while True:
    user_input = input("You: ")
    if user_input=='exit':
        break
    response = model.invoke(user_input)
    print("AI:",response.content)
