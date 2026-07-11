project_map = {

    "Data Scientist": [
        "Spam Classifier",
        "House Price Prediction",
        "Customer Segmentation"
    ],

    "AI Engineer": [
        "Image Classifier",
        "AI Chatbot",
        "Face Recognition System"
    ],

    "Web Developer": [
        "Portfolio Website",
        "E-commerce Website",
        "Blog Application"
    ],

    "Software Engineer": [
        "Library Management System",
        "Bank Management System",
        "Employee Management System"
    ],

    "Full Stack Developer": [
        "E-commerce Website",
        "Food Delivery App",
        "Social Media Platform"
    ],

    "Frontend Developer": [
        "Netflix Clone",
        "Portfolio Website",
        "Weather App"
    ],

    "Backend Developer": [
        "REST API using Spring Boot",
        "Authentication System",
        "Inventory Management API"
    ],

    "DevOps Engineer": [
        "CI/CD Pipeline using Jenkins",
        "Dockerized Web Application",
        "Kubernetes Deployment Project"
    ],

    "Cloud Engineer": [
        "AWS EC2 Deployment",
        "Cloud Storage System",
        "Serverless Web Application"
    ]
}


def recommend_projects(career):
    return project_map.get(
        career,
        ["No projects available"]
    )