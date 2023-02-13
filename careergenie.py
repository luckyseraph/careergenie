import openai
import streamlit as st
import os

openai.api_key = os.environ.get("api_key.openai")

def generate_recommendations(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

st.title("Career Recommendations Generator")

name = st.text_input("Enter your name: ")
major = st.text_input("Enter your major: ")
status = st.selectbox("Are you graduated?", ["Yes", "No"])
interest = st.text_input("Enter your areas of interest: ")
range_ = st.selectbox("Select your desired job range: ", ["Entry-level", "Mid-career", "Executive"])

if st.button("Generate Recommendations"):
    prompt = f"{name} has a degree in {major} and is {status}. They are interested in {interest} and are looking for a job in the {range_} range. Please recommend a few job titles, average salary and potential careers."
    recommendations = generate_recommendations(prompt)
    st.success(recommendations)
