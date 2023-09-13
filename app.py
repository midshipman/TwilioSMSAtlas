import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader

import logging
import sys

#logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
#logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))

#openai.log = "debug"

st.set_page_config(page_title="Twilio SMS Atlas", page_icon="🦙", layout="centered", initial_sidebar_state="auto", menu_items=None)
openai.api_key = st.secrets.openai_key
st.title("Twilio SMS Atlas 🦉 ")
st.info("Find your SMS senders with the Twilio SMS docs, powered by LlamaIndex 💬🦙")
       
if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "In which country do you need  Twilio SMS Senders? I support Japan, Italy, Australia, Germany, UK, Singapore,Ireland"}
    ]

context = """
                You are a Twilio  expert and your job is to answer questions about SMS senders. \
                Assume that all questions are related to the Twilio SMS documents. \
                Keep your answers presise and based on facts, do not hallucinate features. \
                Long code, short code, toll free, and alphanumeric(sender IDs) are 4 types of SMS senders with Twilio, only use these 4 in the answer. \
                Alphanumeric(sender IDs) needs either Pre-registration or Dynamic(meaming you can use any sender ID without pre-registration).))\
                Current supported countries are Japan, Italy, Australia, Germany, UK, Singapore, Ireland\
                Say no if ask for  countires not in the list.
                
            """

answer_format = """
                
                Answer format: \
                First please provide the information in JSON format. The keys should represent the type of phone number or sender ID, \
                and the values should indicate whether Twilio supports it or not. \
                
                
                Include the following keys in your answer: long_code_domestic, long_code_international, short_code, alphanumeric_sender_IDs, toll_free.\
                For short code, please specify either "supported" or "Not Supported", if "Supported" include provisioning time if available.\
                For alphanumeric sender IDs, please specify either "Pre-registration" or "Dynamic", if "Pre-registration" include provisioning time if available\
                Example:
                {
                    "long_code_domestic": "Not Supported",
                    "long_code_international": "Supported",
                    "short_code": "Supported, provisioning time 6-8 weeks",
                    "alphanumeric_sender_IDs": "Dynamic",
                    "toll_free": "Not Supported"
                }

                Then list Use Case Restrictions for each type of supported phone number or sender ID. \
         """

@st.cache_resource(show_spinner=True)
def load_data():
    with st.spinner(text="Loading and indexing the SMS docs – hang tight! This should take 1-2 minutes."):
        reader = SimpleDirectoryReader(input_dir="./twilio", recursive=True)
        docs = reader.load_data()
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-4", temperature=0, system_prompt= context))
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

index = load_data()
#chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True, system_prompt="You are an expert on the Streamlit Python library and your job is to answer technical questions. Assume that all questions are related to the Streamlit Python library. Keep your answers technical and based on facts – do not hallucinate features.")
#chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)
query_engine = index.as_query_engine()

if prompt := st.chat_input("Your question"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("🦉 is Thinking..."):
            prompt = answer_format + "\n\n" + prompt + "\n\n"
            print(prompt)
            #response = chat_engine.chat(prompt)
            response = query_engine.query(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history
