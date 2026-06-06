import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=os.environ["GITHUB_TOKEN"],
)

def learning_path_curator(role: str, certification: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": """You are a Learning Path Curator for enterprise certification programmes.
                Given an employee's role and target certification, you recommend a structured learning path.
                Always cite specific topics, modules, and estimated hours per topic.
                Format your response clearly with sections."""
            },
            {
                "role": "user",
                "content": f"I am a {role} and want to get certified in {certification}. What should I study?"
            }
        ]
    )
    return response.choices[0].message.content

def assessment_agent(topic: str, num_questions: int = 3) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": """You are an Assessment Agent for enterprise certification preparation.
                Generate grounded practice questions with 4 multiple choice options each.
                Always indicate the correct answer and a brief explanation."""
            },
            {
                "role": "user",
                "content": f"Generate {num_questions} practice questions on the topic: {topic}"
            }
        ]
    )
    return response.choices[0].message.content

def study_plan_generator(role: str, certification: str, hours_per_week: int) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": """You are a Study Plan Generator for enterprise learning.
                Create a realistic week-by-week study schedule based on the learner's role,
                target certification, and available hours per week.
                Be specific about what to study each week and set clear milestones."""
            },
            {
                "role": "user",
                "content": f"Create a study plan for a {role} preparing for {certification} with {hours_per_week} hours per week available."
            }
        ]
    )
    return response.choices[0].message.content

def engagement_agent(employee_id: str, meeting_hours: int, focus_hours: int, preferred_slot: str, certification: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": """You are an Engagement Agent for enterprise learning.
                Your job is to analyse an employee's work patterns and recommend
                the best times to study, send reminders, and keep them on track.
                Be specific about days and times. Be realistic about workload.
                Never recommend studying during peak meeting hours.
                Keep advice practical and supportive, not generic."""
            },
            {
                "role": "user",
                "content": f"""Employee ID: {employee_id}
                Meeting hours per week: {meeting_hours}
                Focus hours per week: {focus_hours}
                Preferred learning slot: {preferred_slot}
                Target certification: {certification}
                
                Based on this work pattern, recommend:
                1. The best days and times to schedule study blocks
                2. How to structure reminders without disrupting peak work periods
                3. A realistic weekly study commitment given their workload
                4. Any risk flags if their schedule looks too heavy"""
            }
        ]
    )
    return response.choices[0].message.content


def manager_insights_agent(team_data: list) -> str:
    team_summary = "\n".join([
        f"- {e['employee_id']}: {e['role']}, targeting {e['certification']}, "
        f"practice score {e['practice_score_avg']}%, {e['hours_studied']} hours studied, "
        f"previous outcome: {e['exam_outcome']}"
        for e in team_data
    ])
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": """You are a Manager Insights Agent for enterprise workforce development.
                Analyse team certification data and provide a clear, concise summary for a manager.
                Identify who is on track, who is at risk, and what actions to take.
                Never expose sensitive personal details beyond what is needed.
                Use employee IDs only. Be direct and actionable."""
            },
            {
                "role": "user",
                "content": f"""Here is the current team certification data:

{team_summary}

Provide:
1. Overall team readiness summary
2. Employees on track to pass
3. Employees at risk (low scores or low study hours)
4. Recommended manager actions
5. Predicted team pass rate"""
            }
        ]
    )
    return response.choices[0].message.content

# Orchestrator - runs the full flow
def run_learning_workflow(role: str, certification: str, hours_per_week: int):
    print(f"\n{'='*60}")
    print(f"CERT AGENT SYSTEM - {role} → {certification}")
    print(f"{'='*60}")

    print("\n[1/5] LEARNING PATH CURATOR")
    print("-" * 40)
    path = learning_path_curator(role, certification)
    print(path)

    print("\n[2/5] STUDY PLAN GENERATOR")
    print("-" * 40)
    plan = study_plan_generator(role, certification, hours_per_week)
    print(plan)

    print("\n[3/5] ENGAGEMENT AGENT")
    print("-" * 40)
    engagement = engagement_agent(
        employee_id="EMP-001",
        meeting_hours=22,
        focus_hours=10,
        preferred_slot="Morning",
        certification=certification
    )
    print(engagement)

    print("\n[4/5] ASSESSMENT AGENT")
    print("-" * 40)
    questions = assessment_agent(certification)
    print(questions)

    print("\n[5/5] MANAGER INSIGHTS")
    print("-" * 40)
    team = [
        {"employee_id": "EMP-001", "role": "Cloud Engineer", "certification": "AZ-204",
         "practice_score_avg": 67, "hours_studied": 18, "exam_outcome": "Fail"},
        {"employee_id": "EMP-002", "role": "DevOps Engineer", "certification": "AZ-400",
         "practice_score_avg": 82, "hours_studied": 24, "exam_outcome": "Pass"},
        {"employee_id": "EMP-003", "role": "Data Engineer", "certification": "DP-203",
         "practice_score_avg": 74, "hours_studied": 20, "exam_outcome": "Pass"},
        {"employee_id": "EMP-004", "role": "Cloud Engineer", "certification": "AZ-204",
         "practice_score_avg": 55, "hours_studied": 10, "exam_outcome": "Fail"},
    ]
    insights = manager_insights_agent(team)
    print(insights)


if __name__ == "__main__":
    run_learning_workflow(
        role="Cloud Engineer",
        certification="AZ-204",
        hours_per_week=8
    )