import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder

from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("data/professional_career_dataset.csv")

# Input and Output
X = df["profile"]
y = df["career"]

# Convert text to numbers
vectorizer = TfidfVectorizer()
X_vector = vectorizer.fit_transform(X)

# Encode labels
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vector,
    y_encoded,
    test_size=0.2,
    random_state=42
)

# Models
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Naive Bayes": MultinomialNB(),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    "Linear SVM": LinearSVC()
}

best_model = None
best_accuracy = 0

print("\n========== Model Accuracy ==========\n")

for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"{name}: {accuracy*100:.2f}%")

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model

# Save best model
pickle.dump(best_model, open("professional_career_model.pkl", "wb"))
pickle.dump(vectorizer, open("professional_vectorizer.pkl", "wb"))
pickle.dump(encoder, open("professional_encoder.pkl", "wb"))

print("\n==============================")
print(f"Best Accuracy : {best_accuracy*100:.2f}%")
print("Best Model Saved Successfully!")