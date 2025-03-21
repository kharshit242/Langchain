from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

model=init_chat_model("llama3-8b-8192", model_provider="groq")
chat_history=[]
while True:
        user_input = input("You: ")
        chat_history.append(user_input)
        if user_input=='exit':
            break
        response = model.invoke(chat_history)
        chat_history.append(response)
        print("AI:",response.content)
