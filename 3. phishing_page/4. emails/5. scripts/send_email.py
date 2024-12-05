import smtplib
from email.mime.text import MIMEText

# Configurações do email
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL = 'seu-email@gmail.com'
PASSWORD = 'sua-senha'

# Destinatário e mensagem
to_email = 'destinatario@gmail.com'
subject = 'Verificação de Segurança no Facebook'
body = open('../emails/phishing_email_template.txt', 'r').read()

# Enviar email
msg = MIMEText(body, 'html')
msg['Subject'] = subject
msg['From'] = EMAIL
msg['To'] = to_email

try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, to_email, msg.as_string())
    print("Email enviado com sucesso.")
except Exception as e:
    print(f"Erro ao enviar email: {e}")
