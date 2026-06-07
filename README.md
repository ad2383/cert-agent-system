# Cert Agent System
### Multi-Agent Enterprise Certification Learning System
Built for the Microsoft Foundry Reasoning Agents Hackathon

---

## Overview

Cert Agent System is a multi-agent AI pipeline that helps organisations manage employee certification programmes. Given an employee's role, target certification, and work schedule, the system autonomously generates a personalised learning path, study plan, engagement strategy, practice assessment, and manager-level insights — all through a coordinated chain of specialised AI agents.

---

## Agent Architecture

The system consists of five specialised agents orchestrated in sequence:

### 1. Learning Path Curator
Recommends a structured curriculum mapped to the target certification and employee role. Returns topic breakdowns with estimated study hours per domain.

### 2. Study Plan Generator
Converts the curriculum into a realistic week-by-week schedule based on the employee's available hours per week. Sets clear weekly milestones and exam readiness targets.

### 3. Engagement Agent
Analyses the employee's work patterns — meeting load, focus hours, and preferred learning slot — to recommend optimal study windows and reminder strategies without disrupting peak work periods. Flags risk if workload is too heavy.

### 4. Assessment Agent
Generates grounded multiple-choice practice questions with correct answers and explanations, simulating real certification exam conditions.

### 5. Manager Insights Agent
Takes team-level certification data and produces a concise readiness summary for managers — identifying who is on track, who is at risk, recommended interventions, and a predicted team pass rate.

---

## Multi-Agent Flow

```
User Input (role + certification + hours/week)
        ↓
Learning Path Curator → structured curriculum
        ↓
Study Plan Generator → week-by-week schedule
        ↓
Engagement Agent → work-aware study windows + risk flags
        ↓
Assessment Agent → practice questions + answers
        ↓
Manager Insights Agent → team readiness report
```

---

## Microsoft IQ Integration

This project incorporates the Work IQ intelligence concept through the Engagement Agent, which uses organisational work signals — meeting hours, focus time, and preferred learning slots — to personalise study scheduling and reminder strategies for each employee. This mirrors the Work IQ pattern of grounding agent behaviour in real work context rather than generic scheduling logic.

---

## Synthetic Data

All data used in this project is synthetic and for demonstration purposes only. No real employee data, PII, or confidential information is included.

Example synthetic learner records:

| Employee ID | Role | Certification | Practice Score | Hours Studied | Outcome |
|---|---|---|---|---|---|
| EMP-001 | Cloud Engineer | AZ-204 | 67% | 18 hrs | Fail |
| EMP-002 | DevOps Engineer | AZ-400 | 82% | 24 hrs | Pass |
| EMP-003 | Data Engineer | DP-203 | 74% | 20 hrs | Pass |
| EMP-004 | Cloud Engineer | AZ-204 | 55% | 10 hrs | Fail |

Example synthetic work activity signals:

| Employee ID | Meeting hrs/week | Focus hrs/week | Preferred Slot |
|---|---|---|---|
| EMP-001 | 22 | 10 | Morning |
| EMP-002 | 15 | 18 | Afternoon |

---

## Setup and Installation

### Prerequisites
- Python 3.10+
- A GitHub Personal Access Token (with no special scopes needed)
- Git

### Installation

```bash
git clone https://github.com/ad2383/cert-agent-system
cd cert-agent-system
pip install openai python-dotenv
```

Create a `.env` file in the root directory:

```
GITHUB_TOKEN=your_github_token_here
```

### Run the system

```bash
python agents.py
```

This runs the full 5-agent pipeline for a Cloud Engineer targeting AZ-204 certification with 8 hours per week available.

---

## Example Output

Running the system produces:

- A 115-hour structured curriculum broken down by exam domain
- An 8-10 week study schedule with weekly milestones
- Personalised study window recommendations based on work patterns
- 3 practice exam questions with answers and explanations
- A team readiness report with predicted pass rate and manager action items

---

## Tech Stack

- **Model**: GPT-4o via GitHub Models inference endpoint
- **SDK**: OpenAI Python SDK
- **Orchestration**: Custom Python multi-agent pipeline
- **Platform**: GitHub Codespaces
- **Data**: Synthetic JSON and in-memory records

---

## Project Structure

```
cert-agent-system/
├── agents.py          # All 5 agents + orchestrator
├── test.py            # Connection test script
├── .gitignore         # Excludes .env and secrets
└── README.md          # This file
```

---

## Responsible AI

- All data is synthetic — no PII or real employee records
- Agents never make final decisions autonomously — outputs are recommendations for human review
- Manager insights use employee IDs only, not personal details
- Study recommendations include workload risk flags to avoid burnout

---

## Author

Alona Dhal — Built for the Microsoft Foundry Reasoning Agents Hackathon (Battle #2)
