interview_questions = {

    "Data Scientist": {
        "Technical": [
            "What is feature engineering?",
            "Difference between Regression and Classification?",
            "Explain Bias-Variance Tradeoff."
        ],
        "HR": [
            "Tell me about your Data Science projects.",
            "Why do you want to become a Data Scientist?",
            "Where do you see yourself in 5 years?"
        ]
    },

    "AI Engineer": {
        "Technical": [
            "Explain CNN and RNN.",
            "Difference between TensorFlow and PyTorch.",
            "What is Transfer Learning?"
        ],
        "HR": [
            "Tell me about your AI projects.",
            "Why AI Engineering?",
            "What are your career goals?"
        ]
    },

    "Web Developer": {
        "Technical": [
            "Difference between GET and POST?",
            "Explain REST API.",
            "What is Responsive Web Design?"
        ],
        "HR": [
            "Tell me about your portfolio.",
            "Why Web Development?",
            "Describe a challenging project."
        ]
    },

    "Software Engineer": {
        "Technical": [
            "Explain OOP principles.",
            "What are Design Patterns?",
            "Difference between Stack and Queue?"
        ],
        "HR": [
            "Why Software Engineering?",
            "Tell me about your best project.",
            "How do you debug code?"
        ]
    },

    "Full Stack Developer": {
        "Technical": [
            "Explain MERN Stack.",
            "What is JWT Authentication?",
            "How do you connect frontend and backend?"
        ],
        "HR": [
            "Tell me about your Full Stack project.",
            "Why Full Stack Development?",
            "How do you manage deadlines?"
        ]
    },

    "Frontend Developer": {
        "Technical": [
            "Explain React Hooks.",
            "Difference between Flexbox and Grid?",
            "What is Virtual DOM?"
        ],
        "HR": [
            "How do you improve UI/UX?",
            "Tell me about your frontend project.",
            "Why Frontend Development?"
        ]
    },

    "Backend Developer": {
        "Technical": [
            "What is Spring Boot?",
            "Explain RESTful APIs.",
            "Difference between SQL and NoSQL?"
        ],
        "HR": [
            "Tell me about your backend project.",
            "How do you optimize APIs?",
            "Why Backend Development?"
        ]
    },

    "DevOps Engineer": {
        "Technical": [
            "What is Docker?",
            "Explain Kubernetes.",
            "What is CI/CD?"
        ],
        "HR": [
            "Why DevOps?",
            "Tell me about your deployment experience.",
            "How do you handle production issues?"
        ]
    },

    "Cloud Engineer": {
        "Technical": [
            "Difference between AWS, Azure and GCP?",
            "What is Virtualization?",
            "Explain Load Balancing."
        ],
        "HR": [
            "Why Cloud Engineering?",
            "Tell me about your cloud project.",
            "How do you ensure security in cloud?"
        ]
    }

}


def get_questions(career):

    return interview_questions.get(
        career,
        {
            "Technical": ["No questions available"],
            "HR": ["No questions available"]
        }
    )