import plotly.express as px


def skill_chart(skills, values):

    fig = px.bar(
        x=skills,
        y=values,
        title="Skill Strength Analysis",
        labels={
            "x": "Skills",
            "y": "Level"
        }
    )

    return fig


def readiness_chart(score):

    fig = px.pie(
        values=[score, 100-score],
        names=["Ready", "Need Improvement"],
        title="Career Readiness"
    )

    return fig