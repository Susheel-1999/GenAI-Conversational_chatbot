# GenAI-Conversational_chatbot
A conversational chatbot is an advanced technique for natural language interactions. It has the ability to remember ongoing conversations, mirroring human-like memory in dialogue interactions.

## Steps to run Streamlit app:
1. To create a new OpenAI API key or use an existing one, visit: https://platform.openai.com/api-keys.
   <br><br><br> ![image](https://github.com/Susheel-1999/GenAI-recipe_generator/assets/63583210/3abb56fe-a7b6-4a14-af0a-8befde0af894)

2. Replace the openai key with your own.
3. Create a new environment: <br>```conda create -p genai python==3.9 -y```
4. Activate the environment: <br>```conda activate genai```
5. Install the requirements: <br>```pip install -r requirements.txt```
6. Run the Streamlit application: <br>```streamlit run app.py```

## Output Snapshot:
![image](https://github.com/Susheel-1999/GenAI-Conversational_chatbot/assets/63583210/0da9f1d1-7a7f-4a0b-a72f-7be0f6621d89)
<br><br>
It's fascinating! When I asked, "What do you think about my profession?" the chatbot was able to recall that I am a Data Scientist, a detail I mentioned earlier, and generate a response based on that information.

## About Techniques:
Langchain is a framework for developing applications powered by language models. It enables applications that are context-aware and reason.

1. Importing chat model - We can develop the application by using chat based models easily with the help of langchain. Chat models are often backed by LLMs but tuned specifically for having conversations.
   <br>```from langchain.chat_models import ChatOpenAI```
2. Schema - ChatModels take a list of messages as input and return a message. There are a few different types of messages.
   <br>
   i) _SystemMessage_ : This represents a system message. Only some models support this. This tells the model how to behave. This generally only consists of content. <br>
   ii) _AIMessage_ : This represents a message from the model. This may have additional_kwargs in it - for example functional_call if using OpenAI Function calling.<br>
   iii) _HumanMessage_ : This represents a message from the user. Generally consists only of content.<br>
   other messages like FunctionMessage and ToolMessage are also available.
 <br>```from langchain.schema import HumanMessage, SystemMessage, AIMessage``` <br><br>

Streamlit is an open-source Python library that makes it easy to create and share beautiful, custom web apps for machine learning and data science. In just a few minutes we can build and deploy powerful data apps. 
1. **Session State** - Session State is a way to share variables between reruns, for each user session. Here, it can able to save the conversation we are having with the AI.

# Reference:
Langchain - https://python.langchain.com/docs/get_started/introduction  <br>
OpenAI - https://platform.openai.com/docs/introduction <br>
Streamlit - https://docs.streamlit.io/library/api-reference/session-state

