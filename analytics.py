import random
import openai

openai.api_key = "YOUR_API_KEY"

def simulate_metrics():
    return {
        "open_rate": round(random.uniform(0.2, 0.5), 2),
        "click_rate": round(random.uniform(0.05, 0.2), 2),
        "unsubscribe_rate": round(random.uniform(0.01, 0.05), 2)
    }


def analyze_performance(data):
    prompt = f"Analyze this data and give insights: {data}"

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']
