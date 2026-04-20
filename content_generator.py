import openai
import json

openai.api_key = "YOUR_API_KEY"

def generate_content(topic):
    prompt = f"""
    Topic: {topic}

    Write a 500-word blog post and 3 newsletters for:
    - Creative Agency Owner
    - Marketing Manager
    - Freelancer

    Return JSON format.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return json.loads(response['choices'][0]['message']['content'])
