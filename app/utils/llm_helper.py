import time

PRIMARY_MODEL = "llama-3.3-70b-versatile"
FALLBACK_MODEL = "llama-3.1-8b-instant"


def safe_generate(client, prompt):

    for model in [PRIMARY_MODEL, FALLBACK_MODEL]:

        for attempt in range(3):

            try:

                response = client.chat.completions.create(
                    model=model,
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                return response.choices[0].message.content

            except Exception as e:

                print(
                    f"{model} attempt {attempt + 1} failed: {e}"
                )

                time.sleep(2)

    return "LLM temporarily unavailable."