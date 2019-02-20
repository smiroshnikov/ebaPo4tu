import sendgrid
import os

from sendgrid.helpers.mail import *

os.environ['SENDGRID_API_KEY'] = "NOSUCHKEY!"
sg = sendgrid.SendGridAPIClient(
    api_key=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("postIsrael@post.co.il")
to_email = Email("zer00aeon@gmail.com")
subject = "Zaebali suki "
content = Content("text/plain", "please assist ti my package")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
