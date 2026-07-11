import pandas as pd
import random

careers = {

    "Data Scientist": [
        "Python", "SQL", "Pandas", "NumPy",
        "Machine Learning", "Deep Learning",
        "Statistics", "Power BI", "Data Analysis"
    ],

    "Data Analyst": [
        "Excel", "SQL", "Power BI", "Tableau",
        "Statistics", "Python", "Data Cleaning"
    ],

    "AI Engineer": [
        "Python", "TensorFlow", "PyTorch",
        "OpenCV", "NLP", "Deep Learning",
        "Computer Vision"
    ],

    "ML Engineer": [
        "Python", "Scikit-learn", "XGBoost",
        "Feature Engineering", "Machine Learning",
        "Pandas"
    ],

    "Software Engineer": [
        "Java", "Spring Boot", "Microservices",
        "Docker", "AWS", "SQL"
    ],

    "Full Stack Developer": [
        "HTML", "CSS", "JavaScript",
        "React", "Node.js", "Express",
        "MongoDB"
    ],

    "Frontend Developer": [
        "HTML", "CSS", "JavaScript",
        "React", "Bootstrap",
        "Tailwind CSS"
    ],

    "Backend Developer": [
        "Java", "Spring Boot",
        "REST API", "MySQL",
        "Docker", "Node.js"
    ],

    "DevOps Engineer": [
        "Docker", "Kubernetes",
        "Jenkins", "AWS",
        "Linux", "CI/CD"
    ],

    "Cloud Engineer": [
        "AWS", "Azure",
        "Google Cloud",
        "Docker", "Terraform",
        "Linux"
    ]
}

dataset = []

for career, skills in careers.items():

    for i in range(1000):

        selected_skills = random.sample(
            skills,
            random.randint(4, len(skills))
        )

        profile = " ".join(selected_skills)

        dataset.append({
            "profile": profile,
            "career": career
        })

# Convert to DataFrame
df = pd.DataFrame(dataset)

# Shuffle the dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save as CSV
df.to_csv("data/professional_career_dataset.csv", index=False)

print("✅ Dataset created successfully!")
print(df.head())
print(f"Total Records: {len(df)}")