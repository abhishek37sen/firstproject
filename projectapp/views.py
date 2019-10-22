from django.shortcuts import render
from .models import ServicesData,FeedbackData,Enquiry_Data
from .forms import Feedbackform,EnquiryForm
from django.http.response import HttpResponse
import datetime as dt
date1=dt.datetime.now()
def home_view(request):
    return render(request, 'home.html')

def services_view(request):
    services=ServicesData.objects.all()
    return render(request,'services.html',{'services':services})

def enquiry_view(request):
    if request.method=="POST":
        eform=EnquiryForm(request.POST)
        if eform.is_valid():
            name=request.POST.get('name')
            mobile=request.POST.get('mobile')
            email=request.POST.get('email')
            gender=request.POST.get('gender')
            course=eform.cleaned_data.get('course')
            shifts=eform.cleaned_data.get('shifts')
            start_date=eform.cleaned_data.get('start_date')
            data=Enquiry_Data(
                name=name,
                mobile=mobile,
                email=email,
                gender=gender,
                course=course,
                shifts=shifts,
                start_date=start_date
            )
            data.save()
            eform=EnquiryForm()
            return render(request,'contact.html',{'eform':eform})
        else:
            return HttpResponse('User enter Invalid data')
    else:
        eform=EnquiryForm()
        return render(request, 'contact.html',{'eform':eform})

def gallery_view(request):
    return render(request, 'gallery.html')

def feedback_view(request):
    if request.method=="POST":
        fform=Feedbackform(request.POST)
        if fform.is_valid():
            name=request.POST.get('name')
            rating=request.POST.get('rating')
            feedback=request.POST.get('feedback')
            data=FeedbackData(
                name=name,
                rating=rating,
                date=date1,
                feedback=feedback
            )
            data.save()
            fform=Feedbackform()
            feedbacks=FeedbackData.objects.all()
            return render(request,'feedback.html',{'fform':fform,'feedbacks':feedbacks})
        else:
            return HttpResponse('User Invalid data')
    else:
        fform=Feedbackform()
        feedbacks=FeedbackData.objects.all()
        return render(request,'feedback.html',{'fform':fform,'feedbacks':feedbacks})
