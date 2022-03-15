import smtplib
from email.message import EmailMessage

def alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    # your email and password
    user = 'email sending message'
    password = 'email "app" password'
    
    # setting message subject and receiver to whatever values are passed
    msg['subject'] = subject
    msg['to'] = to
    msg['from'] = user
    
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)
    server.quit()

if __name__ == '__main__':
    alert('your subject here', 'your message here', 'email to get message goes here')
