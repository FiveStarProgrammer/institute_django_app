from django.shortcuts import render
from .models import CourseData,FeedBackData
# Create your views here.
def homepage(request):
    return render(request,'home.html')

def contactpage(request):
    return render(request,'contact.html')

def servicespage(request):
    row = CourseData.objects.all()
    return render(request,'services.html',{'row':row})

def feedbackpage(request):
    if request.method=='GET':
        fbs=FeedBackData.objects.all()
        return render(request,'feedback.html',{"fbs":fbs})
    else:
        FeedBackData(
        feedback=request.POST.get('feed')
        ).save()
        fbs=FeedBackData.objects.all()
        return render(request,'feedback.html',{"fbs":fbs})







def gallerypage(request):
    return render(request,'gallery.html')
