# smpt_sender

Python script to send the same email to many addresses. Email threads get messy when you send a single email to many recipients and they all start answering the email with questions. Sending each recipient their own email keeps the threads separate, but is more time consuming to send out.

## Usage

```bash
python3 smtp_sender.py -t template.txt -e emails.txt -c config.yaml [--cc email1[,email2,email3...]] [--bcc email1[,email2,email3...]]
```

#### template.txt

Contains the email itself. The first row will be used as the subject line and the rest of the rows will be the email body.

```
The first line is used as email subject.
All following lines are part of the email body,
so this

is where

you can type your message.

Cheers
```

#### emails.txt

List all email addresses that should be sent to. One address per line.

```
user1@domain1.com
user2@domain2.com
user3@domain3.com
```

#### config.yaml

Email server credentials.

```
sender_email: your_email@example.com
sender_password: your_email_password
smtp_server: smtp.example.com
smtp_port: 587 
```
