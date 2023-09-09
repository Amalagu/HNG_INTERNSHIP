from django.db import models
from django.utils import timezone
# Create your models here.

class Person(models.Model):
    slack_name = models.CharField(max_length= 100, null=False, blank=False)
    track = models.CharField(max_length=50, blank=False, null=False)
    github_file_url = models.CharField(max_length=200, default='http://github.com/Amalagu')
    github_repo_url = models.CharField(max_length=200, default='http://github.com/Amalagu')
    day = models.DateTimeField(auto_now=True)
    #utc_time = models.DateTimeField(format="%Y-%m-%dT%H:%M:%SZ")
    utc = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=200)

    @property
    def utc_time(self):
        return self.utc.strftime("%Y-%m-%dT%H:%M:%SZ")
    
    @property
    def current_day(self):
        return self.day.strftime('%A')

    
    def __str__(self):
        return self.slack_name