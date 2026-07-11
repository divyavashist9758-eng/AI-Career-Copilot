roadmaps = {

    "Python": [
        "Learn Python Basics",
        "Functions & OOP",
        "File Handling",
        "Practice Python Problems",
        "Build 5 Python Projects"
    ],

    "SQL": [
        "Learn SQL Basics",
        "SELECT, WHERE",
        "GROUP BY, ORDER BY",
        "JOINs",
        "Subqueries",
        "Build Database Project"
    ],

    "Machine Learning": [
        "NumPy",
        "Pandas",
        "Data Preprocessing",
        "Scikit-learn",
        "Regression",
        "Classification",
        "Model Evaluation",
        "Build ML Projects"
    ],

    "Deep Learning": [
        "Neural Networks",
        "TensorFlow / PyTorch",
        "CNN",
        "RNN",
        "Transfer Learning",
        "Build Image Classifier"
    ],

    "Statistics": [
        "Mean, Median, Mode",
        "Probability",
        "Distributions",
        "Correlation",
        "Hypothesis Testing",
        "Regression Analysis"
    ],

    "Pandas": [
        "Series & DataFrame",
        "Data Cleaning",
        "Filtering",
        "Grouping",
        "Merge & Join",
        "Exploratory Data Analysis"
    ],

    "NumPy": [
        "Arrays",
        "Indexing & Slicing",
        "Broadcasting",
        "Mathematical Operations",
        "Linear Algebra",
        "Practice Problems"
    ],

    "Scikit-learn": [
        "Regression",
        "Classification",
        "Clustering",
        "Feature Engineering",
        "Cross Validation",
        "Hyperparameter Tuning"
    ],

    "Data Analysis": [
        "Excel Basics",
        "SQL for Analysis",
        "Pandas",
        "Data Cleaning",
        "EDA",
        "Matplotlib",
        "Power BI Dashboard"
    ],

    "Power BI": [
        "Power BI Interface",
        "Import Data",
        "Power Query",
        "Data Modeling",
        "Relationships",
        "DAX Basics",
        "Dashboard Creation"
    ],

    "Excel": [
        "Basic Formulas",
        "Pivot Tables",
        "Charts",
        "Lookup Functions",
        "Conditional Formatting",
        "Dashboard"
    ],

    "NLP": [
        "Text Cleaning",
        "Tokenization",
        "Stopwords Removal",
        "TF-IDF",
        "Word Embeddings",
        "Transformers",
        "Sentiment Analysis"
    ],

    "Computer Vision": [
        "OpenCV Basics",
        "Image Processing",
        "Object Detection",
        "Image Classification",
        "YOLO",
        "Build CV Project"
    ],

    "OpenCV": [
        "Image Reading",
        "Drawing",
        "Image Transformations",
        "Face Detection",
        "Video Processing",
        "Mini Project"
    ],

    "TensorFlow": [
        "Tensor Basics",
        "Sequential Models",
        "CNN",
        "Model Training",
        "Model Saving",
        "Deploy Model"
    ],

    "PyTorch": [
        "Tensor Basics",
        "Autograd",
        "Neural Networks",
        "CNN",
        "Transfer Learning",
        "Deploy Model"
    ],

    "Streamlit": [
        "Widgets",
        "Layouts",
        "Forms",
        "Charts",
        "Deploy Streamlit App"
    ],

    "Git": [
        "Git Basics",
        "Commit",
        "Branch",
        "Merge",
        "GitHub",
        "Push Projects"
    ],

    "Docker": [
        "Docker Basics",
        "Images",
        "Containers",
        "Dockerfile",
        "Docker Compose"
    ],

    "AWS": [
        "Cloud Basics",
        "EC2",
        "S3",
        "Lambda",
        "Deploy ML Model"
    ],

    "Tableau": [
        "Tableau Basics",
        "Data Connection",
        "Charts",
        "Dashboard",
        "Story Creation"
    ]
}


def generate_roadmap(missing_skills):

    roadmap = {}

    for skill in missing_skills:

        roadmap[skill] = roadmaps.get(
            skill,
            [
                "Learn Basics",
                "Practice Regularly",
                "Build Projects",
                "Master Advanced Concepts"
            ]
        )

    return roadmap