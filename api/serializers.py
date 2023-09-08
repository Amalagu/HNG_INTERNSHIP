from rest_framework import serializers
from .models import Person
import datetime

class PersonSerializer(serializers.ModelSerializer):
    time = datetime.datetime.now()
    class Meta:
        model = Person
        fields = [
        'slack_name', 
        'track', 
        'github_file_url',
        'github_repo_url',
        'current_day',
        'utc_time',
        'status',
        ]
