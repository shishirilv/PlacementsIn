from django import forms
from .models import Profiles
class createProfile(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = [
            'name','branch','jobtitle','cgpa','major','mini','minor','internships','special_courses','email','LinkedIn','org','package_LPA'
        ]

