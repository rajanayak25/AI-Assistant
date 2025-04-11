import streamlit as st
from profile_data import profile

st.set_page_config(page_title="My AI Assistant", layout="centered")

st.title("🧑‍💻 I'm Kishu How can i help you ?")
st.write("Hey Buddy ! Ask me anything about your profile!")

query = st.text_input("Your Question")

def get_info(query):
    query = query.lower()
    if "name" in query:
        return f"My full name is {profile['full_name']}."
    elif "address" in query:
        return f"You're living in {profile['address']}."
    elif "mobile" in query or "phone" in query:
        return f"My mobile number is {profile['mobile_no']}."
    elif "email" in query:
        return f"My email ID is {profile['email']}."
    elif "education" in query:
        return f"My education is {profile['education']}."
    elif "profession" in query or "job" in query:
        return f"I work as a {profile['profession']}."
    elif "hobbies" in query or "hobby" in query:
        return "My hobbies are: " + ", ".join(profile["hobbies"]) + "."
    elif "goal" in query:
        return f": {profile['goals']}."
    else:
        return "Sorry, I couldn't understand that."

if query:
    response = get_info(query)
    st.success(response)
