import streamlit as st
from database import conn, cursor
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import skill_gap
import learning_roadmap
import project_recommendation
import interview_prep
import resume_analyzer
career_df = pd.read_csv("data/careers.csv")


st.set_page_config(page_title="AI Career Copilot", page_icon="🤖")

st.title("🤖 AI Career Copilot")
st.sidebar.title("📋 Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Dashboard",
        "💼 Career Recommendation",
        "📄 Resume Analyzer",
        "🎤 Interview Prep"
    ]
)
if page == "🏠 Dashboard":

    st.header("👤 User Profile")
    name = st.text_input("Enter your Name")
    skills = st.text_input("Enter your Skills")
    interests = st.text_input("Enter your Interests")
    education = st.text_input("Enter your Education")
    if st.button("Save Profile"):
        if name and skills and interests and education:
            cursor.execute(
                "INSERT INTO users (name, skills, interests, education) VALUES (?, ?, ?, ?)",
                (name, skills, interests, education)
            )
            conn.commit()
            st.success("✅ Profile saved successfully!")
        else:
            st.error("Please fill in all fields.")

    st.header("📋 Saved Profiles")

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    for row in rows:
        st.write(f"👤 Name: {row[1]}")
        st.write(f"💻 Skills: {row[2]}")
        st.write(f"🎯 Interests: {row[3]}")
        st.write(f"🎓 Education: {row[4]}")
        st.write("--------------------------------")

       

    st.header("📚 Career Dataset")

    
    st.dataframe(career_df)



if page == "💼 Career Recommendation":

    st.header("💼 Career Recommendation")

    user_skills = st.text_input("Enter your skills (comma separated)")

    if st.button("Recommend Career"):

        user_text = user_skills.lower()

        career_text = career_df["Skills"].fillna("").str.lower()

        vectorizer = TfidfVectorizer()

        vectors = vectorizer.fit_transform([user_text] + career_text.tolist())

        similarity = cosine_similarity(vectors[0:1], vectors[1:]).flatten()

        best_match = similarity.argmax()

        recommended_career = career_df.iloc[best_match]["Career"]
        
        st.success("🎯 Career Recommendation")

        st.markdown(
          f"""
          ## 🚀 {recommended_career}
    
          This career matches your skills and interests.
         """
)
   


        missing_skills = skill_gap.skill_gap(
            [skill.strip() for skill in user_skills.split(",")],
            recommended_career
        )
        st.divider()
        st.subheader("📊 Skill Gap Analysis")

        if missing_skills:
            st.write("### Missing Skills")
            for skill in missing_skills:
                st.write(f"✅ {skill}")

            roadmap = learning_roadmap.generate_roadmap(missing_skills)
            st.divider()
            st.subheader("🗺 Learning Roadmap")

            for skill, steps in roadmap.items():
                st.markdown(f"### {skill}")
                for i, step in enumerate(steps, start=1):
                    st.write(f"{i}. {step}")
            st.divider()
            st.subheader("🚀 Recommended Projects")

            projects = project_recommendation.recommend_projects(
                recommended_career
            )

            for project in projects:
                st.write(f"✅ {project}")
        else:
            st.success("🎉 You already have all the required skills!")
if page == "🎤 Interview Prep":

    st.header("🎤 Interview Preparation")

    career = st.selectbox(
        "Select Career",
        list(interview_prep.interview_questions.keys())
    )

    if st.button("Generate Questions"):

        questions = interview_prep.get_questions(career)

        st.subheader("💻 Technical Questions")

        for q in questions["Technical"]:
            st.write(f"✅ {q}")

        st.subheader("🤝 HR Questions")

        for q in questions["HR"]:
            st.write(f"✅ {q}")
if page == "📄 Resume Analyzer":

    st.header("📄 Resume Analyzer")

    uploaded_file = st.file_uploader(
        "Upload your Resume (PDF)",
        type="pdf"
    )

    if uploaded_file:

        st.success("✅ Resume uploaded successfully!")

        resume_text = resume_analyzer.extract_text(uploaded_file)

        skills = resume_analyzer.extract_skills(resume_text)

        st.subheader("🎯 Skills Found")

        if skills:
            for skill in skills:
                st.write(f"✅ {skill}")
        else:
            st.warning("No skills detected.")
