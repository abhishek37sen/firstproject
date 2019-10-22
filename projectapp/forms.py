from django import forms
from multiselectfield import MultiSelectFormField
class Feedbackform(forms.Form):
    name=forms.CharField(
        label="Enter Your Name:",
        widget=forms.TextInput(
            attrs={
                'class':'form-control','placeholder':'Enter your Name'
            }
        )
    )
    rating=forms.IntegerField(
        label="Enter Your Rating:",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control','placeholder':'Enter Rating'
            }
        )
    )
    feedback=forms.CharField(
        label="Enter YOur Feedback:",
        widget=forms.Textarea(
            attrs={
                'class':'form-control','placeholder':'Enter feedback..'
            }
        )
    )

class EnquiryForm(forms.Form):
    name=forms.CharField(
        label="Enter your Name:",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Name'
            }
        )
    )
    mobile=forms.IntegerField(
        label="Enter your mobile number:",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your Mobile Number'
            }
        )
    )
    email=forms.EmailField(
        label="Enter your Email:",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'your Email'
            }
        )
    )
    Gender_Choices=(
        ('F','Female'),
        ('M','Male')
    )
    gender=forms.ChoiceField(
        widget=forms.RadioSelect,choices=Gender_Choices
    )
    CORSESS_CHOISES = (
        ('PY', "PYTHON"),
        ('DJ', 'Django'),
        ('RA', 'Rest  Api')
    )
    course=MultiSelectFormField(choices=CORSESS_CHOISES)
    SHIFTS_CHOISES = (
        ('Morning', 'Morning shift'),
        ('Afternoon', 'Afternoon_shift'),
        ('Evening', 'Evening_shift'),
        ('Night', 'Night_shift')
    )
    shifts = MultiSelectFormField(choices=SHIFTS_CHOISES)
    start_date=forms.DateField(
        widget=forms.SelectDateWidget()
    )