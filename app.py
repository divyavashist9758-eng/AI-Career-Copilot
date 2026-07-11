import streamlit as st
from database import conn, cursor
import pandas as pd
import skill_gap
import learning_roadmap
import project_recommendation
import interview_prep
import resume_analyzer
import career_chatbot
import career_score
import dashboard_visuals
import pickle

import ai_skill_gap
import ai_interview
import ai_resume
import ai_chatbot
import ai_explainer
import ai_readiness


st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🤖"
)


career_df = pd.read_csv(
    "data/professional_career_dataset.csv"
)


model = pickle.load(
    open("professional_career_model.pkl", "rb")
)

vectorizer_model = pickle.load(
    open("professional_vectorizer.pkl", "rb")
)

encoder = pickle.load(
    open("professional_encoder.pkl", "rb")
)


st.title("🤖 AI Career Copilot")

st.markdown("""
### 🚀 Your AI-Powered Career Guidance Platform

Predict careers • Analyze resumes • Prepare interviews • Track career readiness
""")


st.sidebar.title("📋 Navigation")


page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Dashboard",
        "💼 Career Recommendation",
        "📄 Resume Analyzer",
        "🎤 Interview Prep",
        "💬 Career Chatbot",
        "📈 Career Readiness Score"
    ]
)


# =====================================================
# Dashboard
# =====================================================

if page == "🏠 Dashboard":

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🎯 Career Paths",
            "8+"
        )

    with col2:
        st.metric(
            "💻 Skills",
            "50+"
        )

    with col3:
        st.metric(
            "🤖 AI Features",
            "10"
        )


    st.divider()

    st.subheader(
        "📊 Skills Visualization"
    )


    user_skill_input = st.text_input(
        "Enter skills for visualization (comma separated)"
    )


    if user_skill_input:

        skill_list = [
            skill.strip()
            for skill in user_skill_input.split(",")
        ]

        values = [
            100
            for _ in skill_list
        ]


        chart = dashboard_visuals.skill_chart(
            skill_list,
            values
        )

        st.plotly_chart(chart)



    st.header(
        "👤 User Profile"
    )


    name = st.text_input(
        "Enter your Name"
    )

    skills = st.text_input(
        "Enter your Skills"
    )

    interests = st.text_input(
        "Enter your Interests"
    )

    education = st.text_input(
        "Enter your Education"
    )


    if st.button("Save Profile"):


        if name and skills and interests and education:

            cursor.execute(
                """
                INSERT INTO users
                (name, skills, interests, education)
                VALUES (?, ?, ?, ?)
                """,
                (
                    name,
                    skills,
                    interests,
                    education
                )
            )


            conn.commit()


            st.success(
                "✅ Profile saved successfully!"
            )


        else:

            st.error(
                "Please fill in all fields."
            )



    st.header(
        "📋 Saved Profiles"
    )


    cursor.execute(
        "SELECT * FROM users"
    )


    rows = cursor.fetchall()


    for row in rows:

        st.write(
            f"👤 Name: {row[1]}"
        )

        st.write(
            f"💻 Skills: {row[2]}"
        )

        st.write(
            f"🎯 Interests: {row[3]}"
        )

        st.write(
            f"🎓 Education: {row[4]}"
        )

        st.write(
            "----------------"
        )



    st.header(
        "📚 Career Dataset"
    )


    st.dataframe(
        career_df
    )



# =====================================================
# Career Recommendation
# =====================================================


elif page == "💼 Career Recommendation":


    st.header(
        "💼 Career Recommendation"
    )


    st.subheader(
        "🤖 AI Career Prediction"
    )


    user_profile = st.text_area(
        "Enter your skills, interests, and specialization"
    )


    if st.button("Predict AI Career"):


        if user_profile:


            profile_vector = vectorizer_model.transform(
                [user_profile]
            )


            probabilities = model.predict_proba(
                profile_vector
            )


            top3 = probabilities[0].argsort()[-3:][::-1]


            st.success(
                "🎯 AI Career Prediction"
            )


            for i, idx in enumerate(top3):

                career = encoder.inverse_transform(
                    [idx]
                )[0]


                confidence = probabilities[0][idx] * 100


                st.write(
                    f"### {i+1}. {career}"
                )


                st.progress(
                    confidence / 100
                )


                st.write(
                    f"Confidence: **{confidence:.2f}%**"
                )


            predicted_career = encoder.inverse_transform(
                [top3[0]]
            )[0]


            user_skills = [
                skill.strip()
                for skill in user_profile.split(",")
            ]



            # AI Explanation

            st.divider()

            st.subheader(
                "🤖 Why this Career?"
            )


            reasons = ai_explainer.explain_prediction(
                user_skills,
                predicted_career
            )


            for reason in reasons:

                st.write(
                    reason
                )
# =========================
            # Skill Gap Analysis
            # =========================

            st.divider()

            st.subheader(
                "📊 Skill Gap Analysis"
            )


            required_skills = skill_gap.career_skills[
                predicted_career
            ]


            match_percentage, missing_skills = (
                ai_skill_gap.calculate_skill_gap(
                    user_skills,
                    required_skills
                )
            )


            st.write(
                f"📈 Skill Match Score: {match_percentage}%"
            )


            if missing_skills:

                st.write(
                    "Missing Skills:"
                )


                for skill in missing_skills:

                    st.write(
                        f"❌ {skill}"
                    )



                # =========================
                # Learning Roadmap
                # =========================

                st.divider()
                st.subheader("🗺 Learning Roadmap")

                roadmap = learning_roadmap.generate_roadmap(
                    missing_skills
                )

                for skill, steps in roadmap.items():

                 with st.expander(f"📚 Learn {skill}"):

                     for i, step in enumerate(
                       steps,
                       start=1
                ):
                       st.write(
                           f"{i}. {step}"
                      )


            else:

                st.success(
                    "🎉 You already have all required skills!"
                )



            # =========================
            # Project Recommendation
            # =========================


            st.divider()

            st.subheader(
                "🚀 Recommended Projects"
            )


            projects = project_recommendation.recommend_projects(
                predicted_career
            )


            if projects:

                for project in projects:

                    with st.container():
                         
                         st.success(
                            f"✅ {project}"
                        )


            else:

                st.warning(
                    "No projects available"
                )



        else:

            st.warning(
                "Please enter your profile details."
            )





# =====================================================
# Interview Preparation
# =====================================================


elif page == "🎤 Interview Prep":


    st.header(
        "🎤 AI Interview Preparation"
    )


    career = st.text_input(
        "Enter Career Name"
    )


    if st.button(
        "Generate AI Questions"
    ):


        if career:


            technical, hr = ai_interview.generate_questions(
                career
            )


            st.subheader(
                "💻 Technical Questions"
            )


            for q in technical:

                st.write(
                    f"✅ {q}"
                )



            st.subheader(
                "🤝 HR Questions"
            )


            for q in hr:

                st.write(
                    f"✅ {q}"
                )


        else:

            st.warning(
                "Please enter a career."
            )





# =====================================================
# Resume Analyzer
# =====================================================


elif page == "📄 Resume Analyzer":


    st.header(
        "📄 Resume Analyzer"
    )


    uploaded_file = st.file_uploader(
        "Upload your Resume (PDF)",
        type="pdf"
    )


    if uploaded_file:


        st.success(
            "✅ Resume uploaded successfully!"
        )


        resume_text = resume_analyzer.extract_text(
            uploaded_file
        )


        skills = ai_resume.extract_skills_ai(
            resume_text
        )


        st.subheader(
            "🎯 Skills Found"
        )


        if skills:


            for skill in skills:

                st.write(
                    f"✅ {skill}"
                )


        else:

            st.warning(
                "No skills detected."
            )





# =====================================================
# Career Chatbot
# =====================================================


elif page == "💬 Career Chatbot":


    st.header(
        "💬 AI Career Chatbot"
    )


    user_question = st.text_input(
        "Ask any career-related question"
    )


    if st.button(
        "Get Answer"
    ):


        if user_question:


            answer = ai_chatbot.get_answer(
                user_question
            )


            st.success(
                answer
            )


        else:

            st.warning(
                "Please enter a question."
            )





# =====================================================
# Career Readiness Score
# =====================================================


elif page == "📈 Career Readiness Score":


    st.header(
        "📈 Career Readiness Score"
    )


    user_skills = st.text_input(
        "Enter your skills (comma separated)"
    )


    career = st.selectbox(
        "Select Career",
        list(skill_gap.career_skills.keys())
    )


    projects = st.number_input(
        "Number of Projects Completed",
        min_value=0,
        step=1
    )


    interview_ready = st.checkbox(
        "Completed Interview Preparation?"
    )



    if st.button(
        "Calculate Score"
    ):


        user_skill_list = [
            s.strip()
            for s in user_skills.split(",")
        ]


        score = ai_readiness.calculate_ai_readiness(
            user_skill_list,
            skill_gap.career_skills[career],
            projects,
            interview_ready
        )


        st.subheader(
            "🎯 Career Readiness Score"
        )


        st.progress(
            min(score / 100, 1.0)
        )


        st.success(
            f"Your readiness score is {score}/100"
        )


        chart = dashboard_visuals.readiness_chart(
            score
        )


        st.plotly_chart(
            chart
        )