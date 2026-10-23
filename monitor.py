import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv


load_dotenv()


def send_email_alert(subject: str, message: str) -> None:
    sender = os.getenv("EMAIL_ADDRESS")
    app_password = os.getenv("EMAIL_APP_PASSWORD")
    recipient = os.getenv("ALERT_RECIPIENT")
    smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))

    missing_settings = []

    if not sender:
        missing_settings.append("EMAIL_ADDRESS")
    if not app_password:
        missing_settings.append("EMAIL_APP_PASSWORD")
    if not recipient:
        missing_settings.append("ALERT_RECIPIENT")

    if missing_settings:
        raise RuntimeError(
            "Missing environment variables: "
            + ", ".join(missing_settings)
        )

    email = MIMEMultipart()
    email["From"] = sender
    email["To"] = recipient
    email["Subject"] = subject
    email.attach(MIMEText(message, "plain"))

    with smtplib.SMTP(smtp_server, smtp_port, timeout=30) as connection:
        connection.starttls()
        connection.login(sender, app_password)
        connection.sendmail(sender, recipient, email.as_string())

    print("Email alert sent successfully.")


if __name__ == "__main__":
    send_email_alert(
        subject="Log Monitor Test Alert",
        message="This is a test notification from the Python log monitor.",
    )