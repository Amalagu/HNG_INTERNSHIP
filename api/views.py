from django.shortcuts import render
from .models import Person
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import serializers
import datetime


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
        'utc_time',
        ]




# Create your views here.
def person_api(request):
    if request.method =='GET':
        slack_name=request.GET.get('slack_name')
        track = request.GET.get('track')
        person = Person.objects.filter(slack_name=slack_name, track=track)
        serializer = PersonSerializer(person, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        print(request.data)
        serializer = PersonSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)