from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer


def calculate_ai_readiness(
    user_skills,
    required_skills,
    projects,
    interview_ready
):

    # Convert list to text
    user_text = " ".join(user_skills)
    required_text = " ".join(required_skills)

    # TF-IDF
    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(
        [user_text, required_text]
    )

    # Similarity Score
    similarity = cosine_similarity(
        vectors[0],
        vectors[1]
    )[0][0]

    skill_score = similarity * 60

    project_score = min(projects * 10, 20)

    interview_score = 20 if interview_ready else 0

    total_score = round(
        skill_score +
        project_score +
        interview_score
    )

    return total_score