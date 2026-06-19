import time

def safe_generate(client, prompt):

    for attempt in range(3):

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            print(f"Attempt {attempt+1} failed")

            time.sleep(5)

    return "LLM temporarily unavailable."