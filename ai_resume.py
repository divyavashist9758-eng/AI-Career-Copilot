import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load skills dataset
df = pd.read_csv("data/resume_skills_dataset.csv")

skills = df["skill"].tolist()

vectorizer = TfidfVectorizer()

skill_vectors = vectorizer.fit_transform(skills)


def extract_skills_ai(resume_text):

    resume_vector = vectorizer.transform([resume_text])

    similarity = cosine_similarity(
        resume_vector,
        skill_vectors
    )

    detected_skills = []

    for i, score in enumerate(similarity[0]):

        if score > 0.10:
            detected_skills.append(skills[i])

    return detected_skills