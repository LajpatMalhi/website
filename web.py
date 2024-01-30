import streamlit as st

def main():
    st.title("My Simple Website")

    st.markdown("""
    Welcome to my simple website!
    """)

    st.markdown("---")

    st.header("About Me")
    st.write("""
    My name is John Doe. I'm a web developer based in Example City.
    """)

    st.header("My Projects")
    st.write("""
    - Project 1: [Link to Project 1](#)
    - Project 2: [Link to Project 2](#)
    - Project 3: [Link to Project 3](#)
    """)

    st.header("Contact Me")
    st.write("""
    You can reach me at john.doe@example.com
    """)

if __name__ == "__main__":
    main()
