def create_contact(email, persona):
    print(f"[CRM] Created contact: {email} ({persona})")


def send_newsletter(persona, content):
    print(f"\n[EMAIL] Sending to {persona}")
    print(content[:100] + "...")
