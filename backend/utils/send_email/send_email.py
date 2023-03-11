from django.core.mail import send_mail


def send_email(subject: str, body: str, recipients: list, sender_email: str = 'sofijkasupercool9000@gmail.com'):
    send_mail(subject,
              body,
              sender_email,
              recipients,
              fail_silently=False)
