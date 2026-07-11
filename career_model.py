import pandas as pd

data = pd.read_csv("data/career_recommender.csv")

# Combine useful columns
data["profile"] = (
    data["What are your interests?"].fillna("") + " " +
    data["What are your skills ? (Select multiple if necessary)"].fillna("") + " " +
    data["What is your UG specialization? Major Subject (Eg; Mathematics)"].fillna("")
)

print(data["profile"].head())
# Create career labels

def assign_career(text):
    text = text.lower()

    if "python" in text or "machine learning" in text or "data" in text:
        return "Data Scientist"

    elif "java" in text or "cloud" in text:
        return "Software Engineer"

    elif "web" in text or "html" in text:
        return "Web Developer"

    elif "ai" in text or "deep learning" in text:
        return "AI Engineer"

    else:
        return "Technology Professional"


data["career"] = data["profile"].apply(assign_career)

print(data[["profile", "career"]].head())
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import pickle

# Convert text into numbers
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(data["profile"])


# Convert career names into numbers
encoder = LabelEncoder()

y = encoder.fit_transform(data["career"])


# Train model
model = LogisticRegression(max_iter=1000)

model.fit(X, y)


# Save trained files
pickle.dump(model, open("career_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))
pickle.dump(encoder, open("encoder.pkl", "wb"))


print("ML Model trained successfully!")
