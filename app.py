import streamlit as st
import yaml
from pathlib import Path


def load_data():
    data_file = Path("data/cv.yaml")
    with data_file.open() as f:
        return yaml.safe_load(f)


def show_experience(cv):
    st.header("Experience")
    for exp in cv.get("experience", []):
        role = exp.get("role", "")
        company = exp.get("company", "")
        location = exp.get("location", "")
        start = exp.get("start", "")
        end = exp.get("end", "")
        st.subheader(f"{role} at {company} / {location}")
        st.caption(f"{start} - {end}")
        for item in exp.get("details", []):
            st.write(f"- {item}")


def show_education(cv):
    st.header("Education")
    for edu in cv.get("education", []):
        school = edu.get("school", "")
        degree = edu.get("degree", "")
        start = edu.get("start", "")
        end = edu.get("end", "")
        st.subheader(f"{degree}")
        st.caption(f"{school} ({start} - {end})")
        for item in edu.get("details", []):
            st.write(f"- {item}")


def show_skills(cv):
    st.header("Skills")
    st.write(", ".join(cv.get("skills", [])))


def show_achievements(cv):
    st.header("Achievements and Certificates")
    for item in cv.get("achievements", []):
        st.write(f"- {item}")


def show_contact(cv):
    st.header("Contact")
    contact = cv.get("contact", {})
    if "email" in contact:
        st.write(f"Email: {contact['email']}")
    if "github" in contact:
        st.write(f"GitHub: [{contact['github']}]({contact['github']})")
    if "linkedin" in contact:
        st.write(f"LinkedIn: [{contact['linkedin']}]({contact['linkedin']})")
    if "facebook" in contact:
        st.write(f"Facebook: [{contact['facebook']}]({contact['facebook']})")

    with st.form("contact_form"):
        st.write("Send me a message")
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success("Message sent (demo only)")


def main():
    cv = load_data()
    st.sidebar.title(cv.get("name", "CV"))
    section = st.sidebar.radio("Navigation", (
        "Experience", "Education", "Skills", "Achievements", "Contact"))

    if section == "Experience":
        show_experience(cv)
    elif section == "Education":
        show_education(cv)
    elif section == "Skills":
        show_skills(cv)
    elif section == "Achievements":
        show_achievements(cv)
    else:
        show_contact(cv)


if __name__ == "__main__":
    main()
