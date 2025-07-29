import streamlit as st
from faker import Faker
import random
import pandas as pd

# Generate fake student data
def generate_students(n=15):
    fake = Faker()
    students = []
    for i in range(1, n + 1):
        students.append({
            "ID": i,
            "Name": fake.name(),
            "Problems Solved": random.randint(10, 150),
            "Soft Skills": random.randint(50, 100),
            "Status": random.choice(["Ready", "Not Ready", "Placed"])
        })
    return pd.DataFrame(students)

# Filter students based on criteria
def filter_students(df, min_problems, min_soft_skills):
    return df[(df["Problems Solved"] >= min_problems) & (df["Soft Skills"] >= min_soft_skills)]

def main():
    st.title("🎓 Placement Eligibility Checker")

    # Generate random student data
    df = generate_students(15)

    # Sidebar for eligibility criteria
    st.sidebar.header("Eligibility Criteria")
    min_problems = st.sidebar.slider("Minimum Problems Solved", 0, 150, 50)
    min_soft_skills = st.sidebar.slider("Minimum Soft Skills Score", 0, 100, 70)

    # Filter and show eligible students
    eligible = filter_students(df, min_problems, min_soft_skills)

    st.subheader("Eligible Students")
    if not eligible.empty:
        st.dataframe(eligible)
    else:
        st.warning("No students match the criteria.")

if __name__ == "__main__":
    main()
