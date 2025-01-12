import streamlit as st
import google.generativeai as genai


print('Command for file1')
print('Command for file1')
print('Command for file1')
apikey="#"

print('Command for file2')
genai.configure(api_key=apikey)
print('Command for file2')
model = genai.GenerativeModel('gemini-pro')
print('Command for file2')

//redo the work
print('Another command for file1')
#function to get response from ai
def get_response(q):
print('Another command for file1')
    if q == "" or len(q) < 3:
        return "I can't get you please come again"
    response = model.generate_content(q)
    try:
        return response.text
    except Exception as e:
        return "Sorry , The question is too sensitive."
     

# to handle frontend
st.set_page_config(page_title="Gen Ai")
st.header("Ask anything to Sabari")
input=st.text_input("Input: ",key="input")
submit = st.button("Ask the question")

if submit:
   st.write("Please wait and give some time to sabari to recall")


if submit :

    res = get_response(input) or None
    st.subheader("Response")
    if res:
        st.write(res)
    else:
        st.subheader("Your Questions may senstive ")

