from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db import models


class Webhook(models.Model):
    webhook_type = models.CharField(max_length=255)
    event_type = models.CharField(max_length=255)
    resource_type = models.CharField(max_length=255)
    event_data = models.JSONField()  # This is the trick
    processed = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Webhook: {self.id} - {self.webhook_type}, processed: {self.processed}"


# Signals

# Callback on post save
# Process the webhook data, you could use a task queue like Celery
@receiver(post_save, sender=Webhook)
def my_handler(sender, instance, created, **kwargs):
    if created:
        print("---")
        print(f"Signal received!")
        print("Chaining post processing task for webhook data")
        print(instance)
        print("---")
        pass
