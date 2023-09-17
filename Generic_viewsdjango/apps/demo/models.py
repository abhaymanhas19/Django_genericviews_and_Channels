from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.demo.enum import address_choices

class demo_student(models.Model):
    name=models.CharField(_('Name',),max_length=150)
    rollno=models.IntegerField(_('Roll Number',))
    city=models.CharField(_('City'),choices=address_choices.demo(),max_length=150)
    phone_number=models.IntegerField(_("Phone Number"))


    def __str__(self):
        return self.name
    
