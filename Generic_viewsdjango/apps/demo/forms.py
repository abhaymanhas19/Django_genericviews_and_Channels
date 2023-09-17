from django import forms
from .models import demo_student

class student_form(forms.ModelForm):
    rollno=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'number_class'}))
    class Meta:
        model=demo_student
        fields=['name','rollno','city','phone_number']
        widgets={'name':forms.TextInput(attrs={'class':'name_class','id':'name_id'})}