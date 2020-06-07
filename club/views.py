from django.shortcuts import render
from .models import MeetingType, Meeting, Review
from .forms import ProductForm
from django.contrib.auth.decorators import login_required'

@login_required
def newProduct(request):
     form=ProductForm
     if request.method=='POST':
          form=ProductForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ProductForm()
     else:
          form=ProductForm()
     return render(request, 'club/newproduct.html', {'form': form})

def index (request):
    return render(request, 'club/index.html')

def gettypes(request):
    type_list=ProductType.objects.all()
    return render(request, 'club/types.html' ,{'type_list' : type_list})

def getmeetings(request):
    type_list=ProductType.objects.all()
    return render(request, 'club/meetings.html' ,{'meeting_list' : type_list})

def meetingdetails(request, id):
    meeting=get_object_or_404(Product, pk=id)
    reviews=Review.objects.filter(meeting=id).count()
    context={
        'meeting' : meeting,
        'reviews' : reviews,
    }
    return render(request, 'club/meetingdetails.html', context=context)

def newMeeting(request):
     form=MeetingForm
     if request.method=='POST':
          form=MeetingForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=MeetingForm()
     else:
          form=MeetingForm()
     return render(request, 'club/newmeeting.html', {'form': form})

def loginmessage(request):
    return render(request, 'club/loginmessage.html')

def logoutmessage(request):
    return render(request, 'club/logoutmessage.html')