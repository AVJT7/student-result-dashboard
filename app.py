import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Student Result Dashboard", layout="wide")

st.title("🎓 Student Result Analysis Dashboard")

st.sidebar.header("Enter Marks")

name = st.sidebar.text_input("Student Name")

math = st.sidebar.slider("Math",0,100)
physics = st.sidebar.slider("Physics",0,100)
chemistry = st.sidebar.slider("Chemistry",0,100)
english = st.sidebar.slider("English",0,100)
cs = st.sidebar.slider("Computer Science",0,100)

subjects = ["Math","Physics","Chemistry","English","Computer Science"]
marks = [math,physics,chemistry,english,cs]

df = pd.DataFrame({
    "Subject":subjects,
    "Marks":marks
})

if st.sidebar.button("Generate Result"):

    total = df["Marks"].sum()
    percentage = total/5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 75:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    else:
        grade = "D"

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Marks", total)
    col2.metric("Percentage", round(percentage,2))
    col3.metric("Grade", grade)

    st.subheader("📊 Marks Table")
    st.dataframe(df)

    st.subheader("📈 Bar Chart")

    fig1, ax1 = plt.subplots()
    ax1.bar(df["Subject"], df["Marks"])
    ax1.set_ylabel("Marks")
    ax1.set_title("Subject Performance")

    st.pyplot(fig1)

    st.subheader("🥧 Pie Chart")

    fig2, ax2 = plt.subplots()
    ax2.pie(df["Marks"], labels=df["Subject"], autopct='%1.1f%%')
    ax2.set_title("Marks Distribution")

    st.pyplot(fig2)

    st.subheader("📉 Statistics")

    st.write("Average Marks:", df["Marks"].mean())
    st.write("Highest Marks:", df["Marks"].max())
    st.write("Lowest Marks:", df["Marks"].min())

    csv = df.to_csv(index=False)

    st.download_button(
        label="Download Result CSV",
        data=csv,
        file_name="student_result.csv",
        mime="text/csv",
    )
