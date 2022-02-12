from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .fk import SpanningForeignKey


class Story(models.Model):
    #author = SpanningForeignKey('auth.User', on_delete=models.SET_NULL, default=None, null=True, blank=True, verbose_name='stories')
    #author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='authors')
    #author_id = models.IntegerField('auth.User.id', blank=False)
    author = models.CharField('auth.User.username', max_length=150)
    title = models.CharField(max_length=100)
    text = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=True, blank=False)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title

    #@property
    #def author(self):
    #    return User.objects.get(pk=self.author_id)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.using('default').create(user=instance)