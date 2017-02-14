from flask_mail import Message

from scrapymon import mail
from scrapymon import worker


@worker.task
def send_mail(**kwargs):
    """Send mail."""
    mail.send(Message(**kwargs))
    return 0


@worker.task
def async_test(x, y):
    """Celery test."""
    return x + y