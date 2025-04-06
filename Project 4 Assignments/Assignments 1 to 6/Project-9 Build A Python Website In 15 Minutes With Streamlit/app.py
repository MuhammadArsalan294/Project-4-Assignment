import streamlit as st

# Setting up the page config and title
st.set_page_config(page_title="Arsalan's Portfolio", page_icon="🌟")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "About", "Portfolio", "Contact"))

# Home Page
def home():
    st.title("Welcome to Arsalan's Portfolio Website 🌟")
    st.write("""
    Hello! I am Arsalan, a full-stack developer and AI enthusiast. 
    This is my personal website where I showcase my skills, projects, and how to get in touch with me.
    """)
    st.image("https://cdn.pixabay.com/photo/2024/03/15/19/51/ai-generated-8635685_640.png", width=300)

# About Page
def about():
    st.title("About Me")
    st.write("""
    I am passionate about technology and coding. My expertise lies in Full-Stack Development, 
    Artificial Intelligence, and creating interactive web apps using Python and Streamlit.
    
    ## Skills:
    - Full-Stack Web Development (React, Next.js, Node.js)
    - Python Programming
    - Machine Learning
    - UI/UX Design
    - Data Visualization
    """)

# Portfolio Page
def portfolio():
    st.title("My Projects")
    st.write("""
    Below are some of the projects I've worked on:

    ### 1. E-commerce Website (Next.js, React)
    An e-commerce website for buying and selling fruits.

    ### 2. AI-based Chatbot (Python)
    A chatbot built using AI techniques to answer common queries.

    ### 3. Hangman Game (Python)
    A classic game created using Python.

    ### 4. BMI Calculator (Streamlit)
    A simple BMI calculator app built with Streamlit.
    """)

# Contact Page
def contact():
    st.title("Contact Me")
    st.write("""
    Feel free to reach out to me for any inquiries or collaboration opportunities!

    - **Email:** arsalan@example.com
    - **Phone:** 03021210812
    - **LinkedIn:** [Arsalan's LinkedIn](https://www.linkedin.com/in/arsalan)
    """)

# Display the selected page
if page == "Home":
    home()
elif page == "About":
    about()
elif page == "Portfolio":
    portfolio()
elif page == "Contact":
    contact()

# Run the App

# streamlit run app.py