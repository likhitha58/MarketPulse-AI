from app.config.gemini import client

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain NVIDIA in 3 lines."
)

print(response.text)