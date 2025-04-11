import streamlit as st
from profile_data import profile

st.set_page_config(page_title="My AI Assistant", layout="centered")

st.title("🧑‍💻 I'm Kishu How can i help you ?")
st.write("Hey Buddy ! Have a good day 😊 ")

# Ask user their name
user_name = st.text_input("Please enter your name to begin:")

if user_name:
    st.write(f"👋 Hey {user_name}, how can I help you today?")
    query = st.text_input("Ask something about your profile:")

    def get_info(query):
        query = query.lower()
        if "name" in query:
            return f"Hey {user_name}, your full name is {profile['full_name']}."
        elif "address" in query:
            return f"Hey {user_name}, your address is {profile['address']}."
        elif "mobile" in query or "phone" in query:
            return f"Hey {user_name}, your mobile number is {profile['mobile_no']}."
        elif "email" in query:
            return f"Hey {user_name}, your email ID is {profile['email']}."
        elif "education" in query:
            return f"Hey {user_name}, your education is {profile['education']}."
        elif "profession" in query or "job" in query:
            return f"Hey {user_name}, you work as a {profile['profession']}."
        elif "hobbies" in query or "hobby" in query:
            return f"Hey {user_name}, your hobbies are: " + ", ".join(profile["hobbies"]) + "."
        elif "goal" in query:
            return f"Hey {user_name}, your goal is: {profile['goals']}."
        else:
            return f"Sorry {user_name}, I couldn't understand that."

    if query:
        response = get_info(query)
        st.success(response)
