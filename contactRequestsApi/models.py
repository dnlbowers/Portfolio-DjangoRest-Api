from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


# Create your models here.
class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    reason = models.CharField(max_length=30)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def _send_as_email(self):
        """
        Send request as email
        """
        customer_email = self.email
        subject = render_to_string(
            'contactRequestsApi/email/email_subject.txt',
            {'contact': self})
        body = render_to_string(
            'contactRequestsApi/email/email_body.txt',
            {'contact': self})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customer_email]
        )
        
@receiver(post_save, sender=ContactRequest)
def _post_save_receiver(sender, instance, **kwargs):
    sender._send_as_email(instance)
