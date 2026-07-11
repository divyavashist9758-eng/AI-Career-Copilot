career_skills = {

    "Data Scientist": [
        "Python",
        "SQL",
        "Pandas",
        "NumPy",
        "Machine Learning",
        "Deep Learning",
        "Statistics",
        "Power BI",
        "Data Analysis"
    ],

    "AI Engineer": [
        "Python",
        "TensorFlow",
        "PyTorch",
        "OpenCV",
        "NLP",
        "Deep Learning",
        "Computer Vision"
    ],

    "Web Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Bootstrap",
        "Node.js",
        "MongoDB"
    ],

    "Software Engineer": [
        "Java",
        "Spring Boot",
        "Microservices",
        "Docker",
        "AWS",
        "SQL"
    ],

    "Full Stack Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Node.js",
        "Express",
        "MongoDB"
    ],

    "Frontend Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Bootstrap",
        "Tailwind CSS"
    ],

    "Backend Developer": [
        "Java",
        "Spring Boot",
        "REST API",
        "MySQL",
        "Docker",
        "Node.js"
    ],

    "DevOps Engineer": [
        "Docker",
        "Kubernetes",
        "Jenkins",
        "AWS",
        "Linux",
        "CI/CD"
    ],

    "Cloud Engineer": [
        "AWS",
        "Azure",
        "Google Cloud",
        "Docker",
        "Terraform",
        "Linux"
    ]
}


def skill_gap(user_skills, career):

    required = career_skills.get(career, [])

    missing = []

    for skill in required:

        if skill.lower() not in [s.lower() for s in user_skills]:
            missing.append(skill)

    return missing