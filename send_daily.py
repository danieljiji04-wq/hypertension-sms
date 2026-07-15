import os
from twilio.rest import Client

# Pulled from GitHub Secrets — never hardcoded
TWILIO_SID   = os.environ["TWILIO_SID"]
TWILIO_TOKEN = os.environ["TWILIO_TOKEN"]
TWILIO_FROM  = os.environ["TWILIO_FROM"]

client = Client(TWILIO_SID, TWILIO_TOKEN)

# For now, a simple patient list. Replace with your real enrolled patients.
patients = [
    {"name": "Test", "phone": "+17868062009"},  # put YOUR phone here to test
]

for p in patients:
    message = client.messages.create(
        body=f"Hi {p['name']} 👋 It's your daily check-in from your care team. "
             f"Take 2 minutes to let us know how you're doing: "
             f"https://adherencepilot.app/checkin\n\nReply STOP to opt out.",
        from_=TWILIO_FROM,
        to=p["phone"]
    )
    print(f"Sent to {p['name']}: {message.sid}")
