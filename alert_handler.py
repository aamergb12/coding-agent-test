import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests

class AlertHandler:
    def __init__(self, config):
        self.config = config
        self.alert_history = []

    def send_email_alert(self, subject, message):
        """Send email alerts when thresholds are exceeded"""
        try:
            smtp_server = self.config.get('smtp_server')
            smtp_port = self.config.get('smtp_port')
            sender_email = self.config.get('sender_email')
            receiver_email = self.config.get('receiver_email')
            password = self.config.get('email_password')

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = f"Server Alert: {subject}"

            msg.attach(MIMEText(message, 'plain'))

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, password)
                server.send_message(msg)

            return True
        except Exception as e:
            print(f"Failed to send email alert: {str(e)}")
            return False

    def send_slack_alert(self, message):
        """Send alerts to Slack channel"""
        try:
            webhook_url = self.config.get('slack_webhook_url')
            payload = {'text': message}
            response = requests.post(webhook_url, json=payload)
            return response.status_code == 200
        except Exception as e:
            print(f"Failed to send Slack alert: {str(e)}")
            return False

    def trigger_alert(self, alert_type, subject, message):
        """Handle different types of alerts"""
        self.alert_history.append({
            'type': alert_type,
            'subject': subject,
            'message': message,
            'timestamp': datetime.datetime.now()
        })

        if alert_type == 'email':
            return self.send_email_alert(subject, message)
        elif alert_type == 'slack':
            return self.send_slack_alert(message)
        else:
            print(f"Unsupported alert type: {alert_type}")
            return False

    def get_alert_history(self):
        """Return history of all alerts"""
        return self.alert_history