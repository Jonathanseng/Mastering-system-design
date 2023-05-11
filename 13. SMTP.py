import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up SMTP connection
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('your_email_address@gmail.com', 'your_email_password')

# Set up email message
msg = MIMEMultipart()
msg['From'] = 'your_email_address@gmail.com'
msg['To'] = 'recipient_email_address@example.com'
msg['Subject'] = 'Test Email'
body = 'This is a test email.'
msg.attach(MIMEText(body, 'plain'))

# Send email
text = msg.as_string()
server.sendmail('your_email_address@gmail.com', 'recipient_email_address@example.com', text)

# Close SMTP connection
server.quit()

# In this example, we first set up an SMTP connection using the smtplib module. We then create an email message using the email.mime.text and email.mime.multipart modules, set the message headers, and attach the message body. Finally, we send the email using the SMTP connection and close the connection. Note that you'll need to replace your_email_address@gmail.com and your_email_password with your actual email address and password, respectively, and recipient_email_address@example.com with the recipient's email address.
