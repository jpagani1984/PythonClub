from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re

class MeetingManager(models.Manager):
    def createMeeting(self, postData, user_id):
        response = {
            'status' : False,
            'errors' : []
        }
        if len(postData['title']) < 2:
            response['errors'].append('invalid item FRIEND')
        if len(response['errors']) == 0:
            response['status'] = True
            user_id = Users.objects.get(id = user_id)
            title = Title.objects.create(
                title = postData['title'],
                added_by = user_id
            )
            title.other.add(user_id)
            title.save()
        return response
    def createOther(self, user_id, title_id):
        user_id = Users.objects.get(id = user_id)
        title = Title.objects.get(id = title_id)
        title.other.add(user_id)
        title.save()

    def removeTitle(self, user_id, title_id):
        user_id = Users.objects.get(id = user_id)
        title = Title.objects.get(id = title_id)
        title.other.remove(user_id)
        title.save()
    
    def deleteTitle(self, user_id, title_id):
        title = Title.objects.get(id = title_id)
        title.delete()

class Meeting(models.Model):
    meeting_title = models.CharField(max_length = 255)
    meeting_date = models.DateTimeField(auto_now_add = True)
    meeting_time = models.DateTimeField(auto_now_add = True)
    meeting_location = models.CharField(max_length = 255)
    meeting_agenda = models.CharField(max_length = 255)

class MeetingMinutes(models.Model)
    meeting_id = models.models.ForeignKey(Users, related_name = 'added_by', null=True)
    attendance = models.ManyToManyField(Users, related_name = 'other_user')
    minutes = models.CharField(max_length = 255)

class Resource(models.Model)
    resource_type = models.CharField(max_length = 255)
    URL = models.CharField(max_length = 255)
    date_entered = models.DateTimeField(auto_now_add = True)
    user_id = models.models.ForeignKey(Users, related_name = 'added_by', null=True)
    description = models.CharField(max_length = 255)

class Event(models.Model)
    event_title = models.CharField(max_length = 255)
    event_location = models.CharField(max_length = 255)
    event_date = models.DateTimeField(auto_now_add = True)
    event_time = models.DateTimeField(auto_now_add = True)
    event_description = models.CharField(max_length = 255)
    user_id = models.models.ForeignKey(Users, related_name = 'added_by', null=True)
    
        
