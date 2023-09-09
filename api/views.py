from django.shortcuts import render
from .models import Person
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import serializers
import datetime
from django.utils import timezone


#create your serializers

class PersonSerializer(serializers.ModelSerializer):
    time = datetime.datetime.now()
    class Meta:
        model = Person
        fields = [
        'slack_name',
        'status', 
        'track', 
        'github_file_url',
        'github_repo_url',
        'current_day',
        #'utc_time',
        ]




# Create your views here.
def person_api(request):
    if request.method =='GET':
        slack_name=request.GET.get('slack_name')
        track = request.GET.get('track')
        person = Person.objects.filter(slack_name=slack_name, track=track).first()
        serializer = PersonSerializer(person)
        response_data = {
            "slack_name": serializer.data['slack_name'],
            "current_day": serializer.data['current_day'],
            "utc_time": timezone.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
            "track": serializer.data['track'],
            "github_file_url": serializer.data['github_file_url'],
            "github_repo_url": serializer.data['github_repo_url'],
            "status": 200,
        }
        return JsonResponse(response_data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(request.data)
        serializer = PersonSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)