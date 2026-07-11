import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("data/interview_dataset.csv")

vectorizer = TfidfVectorizer()

career_vectors = vectorizer.fit_transform(df["career"])


def generate_questions(predicted_career):

    query_vector = vectorizer.transform([predicted_career])

    similarity = cosine_similarity(query_vector, career_vectors)

    df["score"] = similarity[0]

    result = df.sort_values(
        by="score",
        ascending=False
    )

    technical = result[
        result["question_type"] == "Technical"
    ]["question"].head(5).tolist()

    hr = result[
        result["question_type"] == "HR"
    ]["question"].head(3).tolist()

    return technical, hr