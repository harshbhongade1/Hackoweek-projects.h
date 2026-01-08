def faq_bot(user_input):
    user_input = user_input.lower()

    if "timing" in user_input or "time" in user_input:
        return "Our institute operates from 9:00 AM to 6:00 PM."

    elif "working day" in user_input or "open" in user_input:
        return "We are open from Monday to Saturday."

    elif "course" in user_input:
        return "We offer courses in Python, Data Science, AI, and Web Development."

    elif "fee" in user_input or "fees" in user_input:
        return "Course fees range from ₹200000 to ₹300000 depending on the course."

    elif "admission" in user_input or "join" in user_input:
        return "You can take admission by visiting our institute or registering online."

    elif "contact" in user_input or "phone" in user_input:
        return "You can contact us at +91-9876543210."

    elif "email" in user_input:
        return "Our email address is info@institute.com."

    elif "location" in user_input or "address" in user_input:
        return "We are located at MG Road, Bangalore."

    elif "online" in user_input:
        return "Yes, we provide both online and offline classes."

    elif "batch size" in user_input:
        return "Each batch has a maximum of 25 students."

    elif "faculty" in user_input or "trainer" in user_input:
        return "Our trainers are industry professionals with 5+ years of experience."

    elif "certificate" in user_input:
        return "Yes, we provide a course completion certificate."

    elif "installment" in user_input:
        return "Yes, fee installments are available."

    elif "demo" in user_input:
        return "Yes, we offer a free demo class."

    elif "placement" in user_input:
        return "We provide placement assistance with interview preparation."

    else:
        return "Sorry, I couldn't understand your question. Please ask about timings, fees, courses, or contact details."


print("FAQ Bot: Hello! Ask me about the institute.")

while True:
    user = input("You: ")
    if user.lower() in ["exit", "quit", "bye"]:
        print("FAQ Bot: Thank you! Have a great day.")
        break
    print("FAQ Bot:", faq_bot(user))




import streamlit as st

# --- BACKEND LOGIC ---
def chatbot(user_input):
    user_input = user_input.lower()

    if "timing" in user_input or "time" in user_input:
        return "Our institute is open from 9 AM to 6 PM, Monday to Saturday."
    elif "working days" in user_input or "open" in user_input:
        return "We are open from Monday to Saturday."
    elif "courses" in user_input or "course" in user_input:
        return "We offer courses in Python, Data Science, Web Development, and AI."
    elif "fees" in user_input or "fee" in user_input:
        return "Course fees range from ₹200000 to ₹300000 depending on the course."
    elif "admission" in user_input or "join" in user_input:
        return "You can take admission by visiting our institute or applying online."
    elif "contact" in user_input or "phone" in user_input:
        return "You can contact us at +91 98765 43210."
    elif "email" in user_input:
        return "Our email ID is info@abcinstitute.com."
    elif "address" in user_input or "location" in user_input:
        return "We are located at MG Road, Bengaluru."
    elif "online" in user_input:
        return "Yes, we provide online classes."
    elif "offline" in user_input:
        return "Yes, offline classroom training is available."
    elif "faculty" in user_input or "teacher" in user_input:
        return "Our faculty consists of experienced industry professionals."
    elif "duration" in user_input:
        return "Course duration ranges from 2 to 6 months."
    elif "certificate" in user_input:
        return "Yes, we provide a course completion certificate."
    elif "installment" in user_input:
        return "Yes, fees can be paid in installments."
    elif "demo" in user_input:
        return "Yes, we offer a free demo class."
    else:
        return "Sorry, I didn't understand. Please ask about courses, fees, timing, or contact details."

# --- FRONTEND UI ---
st.set_page_config(page_title="ABC Institute Chatbot", page_icon="🎓")

st.title("🎓 Symbiosis Institute FAQ Assistant")
st.markdown("Welcome to Symbiosis Institute of Technology! Ask me anything about our courses, fees, or timings.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("How can I help you today?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get response from chatbot backend
    response = chatbot(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
