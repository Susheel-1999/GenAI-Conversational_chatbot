import streamlit as st
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI
import os

# Environmental variables
os.environ["HUGGINGFACEHUB_API_TOKEN"] = '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'


# LLM
llm = ChatOpenAI(temperature = 0.7, model_name = "gpt-3.5-turbo", openai_api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")) 
system_msg = "You are a helpful assistant"

def display_chat_history(history):
    for message in history[::-1]:
        if isinstance(message, HumanMessage):
            st.write(f"Me : {message.content}")
        elif isinstance(message, AIMessage):
            st.write(f"AI : {message.content}")
        else:
            pass

def main():
    # UI
    st.set_page_config(page_title="chatbot")
    st.title("Conversational ChatBot")
    st.caption("A conversational chatbot is an advanced technique for natural language interactions. It has the ability to remember ongoing conversations, mirroring human-like memory in dialogue interactions.")
    st.subheader("AI ChatBot")

    # Initialize session state
    if 'history' not in st.session_state:
        st.session_state.history = [SystemMessage(content = system_msg)]
    
    user_msg = st.text_input("Me: ", key="input")
    st.session_state['history'].append(HumanMessage(content = user_msg))
    llm_response = llm(st.session_state['history'])
    st.session_state['history'].append(AIMessage(content = llm_response.content))
    display_chat_history(st.session_state.history)

if __name__ == '__main__':
    main()