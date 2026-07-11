import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
chatbot_df = pd.read_csv("data/chatbot_dataset.csv")
print(chatbot_df.head())
print(chatbot_df.columns)

# Remove empty rows
chatbot_df = chatbot_df.dropna()

# Convert to string
chatbot_df["question"] = chatbot_df["question"].astype(str)
chatbot_df["answer"] = chatbot_df["answer"].astype(str)

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

question_vectors = vectorizer.fit_transform(
    chatbot_df["question"]
)


def get_answer(user_question):

    user_vector = vectorizer.transform(
        [user_question]
    )

    similarity = cosine_similarity(
        user_vector,
        question_vectors
    )

    index = similarity.argmax()

    return chatbot_df.iloc[index]["answer"]