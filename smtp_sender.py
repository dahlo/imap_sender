import smtplib
import yaml
import argparse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

# Function to read the content of a file
def read_file_content(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

# Function to send email
def send_email(sender_email, sender_password, receiver_email, subject, body, smtp_server, smtp_port, cc_email=None, bcc_email=None):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    if cc_email:
        message['Cc'] = cc_email
    if bcc_email:
        message['Bcc'] = bcc_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(message)
    server.quit()

# Parse command line arguments
parser = argparse.ArgumentParser(description='Send emails using SMTP.')
parser.add_argument('--template', '-t', required=True, help='Path to the email template file')
parser.add_argument('--emails', '-e', required=True, help='Path to the email list file')
parser.add_argument('--config', '-c', required=True, help='Path to the YAML config file')
parser.add_argument('--dry-run', '-d', action='store_true', help='Print the emails instead of sending them')
parser.add_argument('--cc', help='CC email (comma separated)')
parser.add_argument('--bcc', help='BCC email (comma separated)')
args = parser.parse_args()

# Read YAML config file
with open(args.config, 'r') as file:
    config = yaml.safe_load(file)

# Read template file
template_lines = read_file_content(args.template)
subject = template_lines[0].strip()
body = ''.join(template_lines[1:]).strip()

# Read emails file
with open(args.emails, 'r') as file:
    receiver_emails = file.readlines()

# Send emails
for receiver_email in receiver_emails:

    if args.dry_run:
        print(f'Sending email to {receiver_email.strip()} (cc: {args.cc}, bcc: {args.bcc})')
        print(f'Subject: {subject}')
        print(f'Body: {body}')
        continue
    else:
        send_email(config['sender_email'], config['sender_password'], receiver_email.strip(), subject, body, config['smtp_server'], config['smtp_port'], cc_email=args.cc, bcc_email=args.bcc)
        print(f'Email sent to {receiver_email.strip()}')

print('All emails sent successfully!')

