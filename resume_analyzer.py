import PyPDF2
import spacy

nlp = spacy.load("en_core_web_sm")

skills_list = [
    "Python",
    "SQL",
    "Machine Learning",
    "Deep Learning",
    "Pandas",
    "NumPy",
    "TensorFlow",
    "PyTorch",
    "NLP",
    "Java",
    "HTML",
    "CSS",
    "JavaScript",
    "React"
]


def extract_text(pdf_file):

    reader = PyPDF2.PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


def extract_skills(text):

    doc = nlp(text)

    found_skills = []

    text = text.lower()

    for skill in skills_list:
        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills
