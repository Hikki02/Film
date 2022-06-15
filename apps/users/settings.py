from decouple import config
from django.core.mail import EmailMessage


class Email:
    """Email send message function"""

    def __init__(self, user) -> None:
        self.user = user

    def send_email(self, email_mess: EmailMessage) -> None:
        email_mess.send()

    def get_message_data(self) -> dict[str, str]:
        abs_url = config('ABS_URL') + '?token=' + \
                  self.user.get_tokens().get('access', None)
        email_body = f"""
        Hello {self.user.username}, Use this link to activate your email
        {abs_url}
        """
        data = {
            'body': email_body, 'to': [self.user.email],
            'subject': 'Verify your email'
        }
        return data

    def send(self):
        data = self.get_message_data()
        self.send_email(EmailMessage(**data))
