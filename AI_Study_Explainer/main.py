from groq import Groq
import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("api_key")
print(api_key)


client = Groq(api_key=api_key)




st.title("AI Study Explainer")

st.header("Hi, Students!\nI will help you with your studies.")

ques = st.text_area("Enter your question:")

classU = st.selectbox("Select your class:",["Class 1","Class 2","Class 3","Class 4","Class 5","Class 6","Class 7","Class 8","Class 9","Class 10","Class 11","Class 12"]) 
subject = classU = st.selectbox("Select your subject:",["Science","Social Studies","Maths","English","Computer","Economics","Commerce"]) 
mode = st.selectbox("Select the mode:",["Simple","Step-by-step","Quick Revision"]) 
length = st.selectbox("Lenght:",["Short","Medium","Detailed"])
examples = st.checkbox("Include Examples") 
button = st.button("Explain Now!")



if button:
    with st.spinner("Explaning..."):

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": f'''You are a school study explainer.

        Follow the options strictly.

        Class: {classU}
        Subject: {subject}
        Mode: {mode}
        Length: {length}
        Examples: {examples}

        Rules:
        - Use class-appropriate language.
        - Stay within the subject.
        - Follow the mode exactly.
        - Adjust detail by length.
        - If Examples = true, give 1–2 simple examples.
        - If Examples = false, give no examples.
        - Keep it clear and exam-focused.
        - End with a short “Quick Revision”.
        '''},
                {"role": "user", "content": f"Explain: {ques}"}
            ],
        )

        st.text_area("Explaination",response.choices[0].message.content,height=300,disabled=True)



