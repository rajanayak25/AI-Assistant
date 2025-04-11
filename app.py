import streamlit as st

st.set_page_config(page_title="My AI Assistant", layout="centered")

st.title("🧑‍💻 I'm Kishu How can I help you ?")
st.write("Hey Buddy ! Have a good day 😊 ")

# User profile dictionary
profiles = {
    "rajesh": {
        "address": "Warangal, Telangana",
        "profession": "Software Engineer at Quadrant Technologies, Hyderabad",
        "goals": "You want to become an AI expert and Service Now Developer"
    },
    "chandu": {
        "address": "Nizamabad, Telangana",
        "profession": "Senior Software Engineer at Quadrant Technologies, Hyderabad",
        "goals": "You are already a play boy, wishing you more attraction towards you"
    },
    "gopi": {
        "address": "Tirupathi, Andhra Pradesh",
        "profession": "Technical Analyst at Quadrant Technologies, Hyderabad",
        "goals": "You want to become a big business giant"
    },
    "sandeep": {
        "address": "Karimnagar, Telangana",
        "profession": "Software Engineer at Quadrant Technologies, Hyderabad",
        "goals": "You want to become a Bank Employee but unfortunately became an IT employee"
    },
    "venkat": {
        "address": "Hyderabad, Telangana",
        "profession": "Software Engineer at Quadrant Technologies, Hyderabad",
        "goals": "You want to become Technical Lead at QR"
    },
    "srikanth": {
        "address": "Hyderabad, Telangana",
        "profession": "Technical Team Lead at Quadrant Technologies, Hyderabad",
        "goals": "You want to become an Expert and you are willing to fly USA"
    }
}

# Ask user their name
user_name = st.text_input("Please enter your name to Bayya:")

if user_name:
    lower_name = user_name.lower()
    if lower_name in profiles:
        st.write(f"👋 Hey {user_name}, how can I help you today?")
        query = st.text_input("Ask something about your profile:")

        def get_info(query):
            query = query.lower()
            data = profiles[lower_name]
            if "name" in query:
                return f"Hey {user_name}, your name is {user_name}."
            elif "address" in query:
                return f"Hey {user_name}, your address is {data['address']}."
            elif "profession" in query or "job" in query:
                return f"Hey {user_name}, you work as a {data['profession']}."
            elif "goal" in query:
                return f"Hey {user_name}, your goal is: {data['goals']} 😊."
            else:
                return f"Sorry {user_name}, I couldn't understand that."

        if query:
            response = get_info(query)
            st.success(response)
    else:
        st.warning("Sorry, you are a outside user !.")
