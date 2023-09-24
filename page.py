# import openai
# import streamlit as st


# st.title("Isolated Falcons")


# openai.api_key =  st.secrets["OPENAI_API_KEY"]

# if "openai_model" not in st.session_state:
#     st.session_state["openai_model"] = "gpt-3.5-turbo"


# # with st.chat_message(name="user",avatar="👦"):
# #     st.write("Hello :wave:")   

# #history starts
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# #history session
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])


# #chat input
# if prompt := st.chat_input("What's Up ?"):
#     with st.chat_message("user"):
#         st.markdown(prompt)
#     # with st.spinner("Thinking..."):    
#     st.session_state.messages.append({"role": "user", "content": prompt})


#     # response = f"Echo: {prompt}"
        
#     # with st.chat_message("assistant",avatar="🤖"):
#     #      st.markdown(response)

#     # st.session_state.messages.append({"role": "assistant", "content": response})

#     with st.chat_message("assistant"):
#         message_placeholder = st.empty()
#         full_response = ""
#         for response in openai.ChatCompletion.create(
#             model=st.session_state["openai_model"],
#             messages=[
#                 {"role": m["role"], "content": m["content"]}
#                 for m in st.session_state.messages
#                 ],
#                 stream = True,
#         ):
#             full_response += response.choices[0].delta.get("content","")
#             message_placeholder.markdown(full_response + " ")
#         message_placeholder.markdown(full_response)
#         st.session_state.messages.append({"role": "assistant", "content": full_response})


#New UI

import openai
import streamlit as st
from streamlit_chat import message

openai.api_key =  st.secrets["OPENAI_API_KEY"]

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
        n = 1,
        stop  = None,
    )

    message = completions.choices[0].text
    return message

st.title("Isolated Falcons")

st.write("""
    ## Chatbot
"""
)

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text= st.text_input("You :","What's Up ?",key="input")
    return input_text

user_input = get_text()

if user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state.generated:

    for i in range(len(st.session_state.generated)-1,-1,-1):
        message(st.session_state.generated[i],key=str(i))
        message(st.session_state.past[i],is_user=True,key=str(i) + '_user')