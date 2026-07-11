def calculate_score(user_skills, required_skills, projects=0, interview_ready=False):

    # Skill match percentage
    matched = 0

    for skill in required_skills:
        if skill.lower() in [s.lower() for s in user_skills]:
            matched += 1

    if len(required_skills) > 0:
        skill_score = (matched / len(required_skills)) * 60
    else:
        skill_score = 0


    # Project score (20 points)
    if projects >= 3:
        project_score = 20
    elif projects > 0:
        project_score = 10
    else:
        project_score = 0


    # Interview preparation score (20 points)
    if interview_ready:
        interview_score = 20
    else:
        interview_score = 0


    total_score = skill_score + project_score + interview_score

    return round(total_score)