# Log Monitor

A Python project for sending email notifications when important errors are detected in application log files.

## Current status

The project currently includes:

- Gmail SMTP email notifications
- Secure configuration through environment variables
- A sample application log at `logs/application.log`
- Project dependencies for file monitoring with `watchdog`

The current `monitor.py` sends a test email. Continuous log monitoring will be added in a later step.

## Requirements

- Python 3.10 or newer
- A Gmail account
- Google 2-Step Verification enabled
- A Google App Password

## Setup

Clone the repository and open its directory:

```powershell
git clone https://github.com/OneAbhik/log-monitor.git
Set-Location .\log-monitor
```

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Configuration

Create a file named `.env` in the project root:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_APP_PASSWORD=your_google_app_password
ALERT_RECIPIENT=recipient_email@example.com
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

`EMAIL_APP_PASSWORD` must be a Google App Password, not your regular Gmail password.

Never commit `.env` to Git. It is excluded by `.gitignore`.

## Run the email test

With the virtual environment activated, run:

```powershell
python .\monitor.py
```

A successful run prints:

```text
Email alert sent successfully.
```

Check the recipient's inbox, including the Spam or Junk folder.

## Project structure

```text
log_monitor/
├── .env                  # Local credentials; not committed
├── .gitignore
├── logs/
│   └── application.log   # Sample log file
├── monitor.py            # Email notification code
├── requirements.txt
└── README.md
```

## Security

- Use a Google App Password instead of your normal Gmail password.
- Keep `.env` private.
- Do not share credentials in source code, issues, or pull requests.
- Revoke the App Password if it is accidentally exposed.

## License

No license has been selected for this project yet.
