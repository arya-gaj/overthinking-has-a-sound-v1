def send_email(recipient: str, subject: str, body: str) -> str:
    print(f"DEBUG: Calling send_email to {recipient} with subject '{subject}'...")
    return f"Email sent successfully to {recipient} with subject: '{subject}'."
