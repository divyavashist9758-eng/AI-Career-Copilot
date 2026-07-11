from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_skill_gap(user_skills, required_skills):

    user_text = " ".join(user_skills)

    required_text = " ".join(required_skills)


    vectorizer = TfidfVectorizer()


    vectors = vectorizer.fit_transform(
        [user_text, required_text]
    )


    similarity = cosine_similarity(
        vectors[0],
        vectors[1]
    )[0][0]


    match_percentage = round(similarity * 100, 2)


    missing_skills = []

    for skill in required_skills:

        if skill.lower() not in [
            s.lower() for s in user_skills
        ]:
            missing_skills.append(skill)


    return match_percentage, missing_skills