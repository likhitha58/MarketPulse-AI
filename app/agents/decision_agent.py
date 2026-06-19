from app.config.gemini import client
import time


def decision_agent(state):

    prompt = f"""
You are a senior investment committee member.

Research Report:
{state['research_report']}

Financial Report:
{state['financial_report']}

News Intelligence:
{state['news_report']}

Provide:

1. Key Positives
2. Key Risks
3. Final Recommendation

Recommendation:
BUY / HOLD / SELL

Explain your reasoning.
"""

    response = None

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            break

        except Exception as e:

            print(f"Attempt {attempt + 1} failed: {e}")

            time.sleep(5)

    if response is None:
        raise Exception(
            "Gemini unavailable after 3 attempts"
        )

    state["final_recommendation"] = response.text

    return state