from django import forms
from .models import Meeting, MeetingType, Review

class MeetingForm(forms.ModelForm):
    class Meta:
        model=Meeting
        fields='__all__'_'