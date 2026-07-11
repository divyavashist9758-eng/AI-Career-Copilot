career_responses = {

    "How do I become an AI Engineer?":
    """
    1. Learn Python
    2. Learn Machine Learning
    3. Learn Deep Learning
    4. Build AI Projects
    5. Practice Interview Questions
    """,

    "How do I become a Data Scientist?":
    """
    1. Learn Python
    2. Learn SQL
    3. Learn Statistics
    4. Learn Machine Learning
    5. Build Data Science Projects
    """,

    "How do I become a Web Developer?":
    """
    1. Learn HTML
    2. Learn CSS
    3. Learn JavaScript
    4. Learn React
    5. Build Web Projects
    """
}


def get_response(question):

    return career_responses.get(
        question,
        "Sorry, I don't know the answer yet."
    )