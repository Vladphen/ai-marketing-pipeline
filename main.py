from content_generator import generate_content
from crm import create_contact, send_newsletter
from analytics import simulate_metrics, analyze_performance
import json

PERSONAS = [
    "Creative Agency Owner",
    "Marketing Manager",
    "Freelancer"
]

def run_pipeline(topic):
    print(f"Generating content for: {topic}")

    content = generate_content(topic)

    with open("storage.json", "w") as f:
        json.dump(content, f, indent=2)

    results = {}

    for persona in PERSONAS:
        create_contact(f"{persona.lower().replace(' ', '')}@test.com", persona)

        newsletter = content["newsletters"][persona]

        send_newsletter(persona, newsletter)

        metrics = simulate_metrics()
        results[persona] = metrics

    insights = analyze_performance(results)

    print("\n=== PERFORMANCE ===")
    print(results)

    print("\n=== INSIGHTS ===")
    print(insights)


if __name__ == "__main__":
    run_pipeline("AI in Creative Automation")
