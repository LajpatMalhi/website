import streamlit as st

def generate_cv(name, email, phone, education, experience, skills):
    cv = f"""
    # Curriculum Vitae

    ## Personal Information
    - **Name:** {name}
    - **Email:** {email}
    - **Phone:** {phone}

    ## Education
    - {education}

    ## Experience
    - {experience}

    ## Skills


    
    - {skills}
    """
    return cv

def main():
    st.title("CV Generator")

    # User input fields
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone")
    education = st.text_area("Education", "Enter your educational qualifications")
    experience = st.text_area("Experience", "Enter your work experience")
    skills = st.text_area("Skills", "Enter your skills separated by commas")

    # Generate CV button
    if st.button("Generate CV"):
        if name and email and phone and education and experience and skills:
            generated_cv = generate_cv(name, email, phone, education, experience, skills)
            st.markdown(generated_cv, unsafe_allow_html=True)
        else:
            st.warning("Please fill in all fields to generate CV.")

if __name__ == "__main__":
    main()
