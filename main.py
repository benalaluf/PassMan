import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the SMTP server details
smtp_server = 'outlook.com'  # Outlook/Hotmail SMTP server
port = 587  # Port for TLS encryption
sender_email = 'passman_test@hotmail.com'
password = 'Passman12345'  # Replace 'your_password' with your actual password

# Create a message
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = 'iben.alaluf@gmail.com'
message['Subject'] = 'Subject of the Email'

# Add body to email
body = "hi ben, this is a test email from Passman."
message.attach(MIMEText(body, 'plain'))

# Connect to the SMTP server
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()  # Start TLS encryption
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, 'iben.alaluf@gmail.com', text)
