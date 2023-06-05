from pyvas import Vas5
import smtplib
from email.mime.text import MIMEText

# Configurer les informations de connexion OpenVAS
HOST = 192.30.0.4
PORT = 443
USERNAME = 'admin'
PASSWORD = 'keycekeycekeyce'

# Configurer les informations de l'e-mail
# SMTP_SERVER = 'your_smtp_server'
# SMTP_PORT = 000
# EMAIL_FROM = 'your_email_from'
# EMAIL_TO = 'your_email_to'
# EMAIL_SUBJECT = 'Rapport de scan OpenVAS'

# Se connecter à OpenVAS
openvas = Vas5(HOST, PORT, USERNAME, PASSWORD)

# Lancer le scan sur la plage d'adresses IP
scan_result = openvas.launch_scan(target='10.0.2.15')

# Récupérer les résultats du scan
report = openvas.get_report(scan_result.report_id)

# # Envoyer les résultats par e-mail
# message = MIMEText(report)
# message['From'] = EMAIL_FROM
# message['To'] = EMAIL_TO
# message['Subject'] = EMAIL_SUBJECT

# smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
# smtp.send_message(message)
# smtp.quit()

print(report)