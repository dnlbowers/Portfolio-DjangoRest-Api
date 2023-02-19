from django.db import models
from autoslug import AutoSlugField
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_delete
import cloudinary
from django.dispatch import receiver


# Create your models here.
STATUS = ((0, 'hidden'), (1, 'Public'), (2, 'coming soon'))

class Project(models.Model):
    """"
    Holds project details in DB.
    """

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    slug = AutoSlugField(
        populate_from='title',
        unique_with='repo_url',
    )
    hosted_url = models.URLField(max_length=200, blank=True)
    repo_url = models.URLField(max_length=200, blank=True)
    screenshot = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    completion_date = models.DateField(blank=True, null=True)

    class meta:
        ordering = ['-completion_date']
        verbose_name_plural = 'projects'

    def __str__(self):
        return self.title


@receiver(pre_delete, sender=Project)
def project_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.screenshot.public_id)
