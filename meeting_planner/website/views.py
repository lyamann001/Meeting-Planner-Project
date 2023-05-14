from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting
# Create your views here.


def welcome(request):
    return render(request,
                  'website/welcome.html',
                  {
                      'message': 'Welcome to the Meeting Planner',
                      'num_meetings': Meeting.objects.count(),
                      'meetings': Meeting.objects.all()
                  })


def date(request):
    return HttpResponse(f'This page was served at {str(datetime.now())}')


def about(request):
    return HttpResponse('This page powered by Tyson Solution')