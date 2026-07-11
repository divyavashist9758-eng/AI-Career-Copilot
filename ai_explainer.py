def explain_prediction(user_skills, predicted_career):

    reasons = []

    for skill in user_skills:

        reasons.append(f"✔ {skill} detected in your profile.")

    reasons.append(
        f"✔ These skills closely match the requirements of a {predicted_career}."
    )

    reasons.append(
        "✔ AI model predicted this career based on your overall profile."
    )

    return reasons