from typing import Any, Dict, List, Optional, Type
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView,FormView
from apps.demo.models import demo_student
from django.views import View
from django.conf import settings
from django import forms
from .forms import student_form

# Create your views here.
class Getview(ListView):
    model=demo_student
    # template_name_suffix='get'
    template_name='demo/show.html'
    # context_object_name='student'

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset() # or custom return 
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context=super().get_context_data(**kwargs)
        context['new']="ksjfie"
        return context

    # def get_template_names(self):
    #     if self.request.COOKIES['user']=="abhiy":
    #         template_name='demo/templatename.html'
    #     else:
    #         template_name=self.template_name
    #     return [template_name]
    

class Detailview(DetailView):   
    model=demo_student
    # template_name=""
    # context_object_name=""
    # pk_url_kwarg=""


class Createview(CreateView):
    # form_class=student_form
    model=demo_student  
    fields=['name',"rollno","city","phone_number"]
    # template_name='demo/create.html'
    success_url='/create/'

    def get_form(self):
        form=super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'form-control'})
        return form

class Formview(FormView):
    form_class=student_form
    template_name='demo/demo_student_form.html'
    success_url='/form/'

    def form_valid(self,form):
        print(form.cleaned_data['name'])
        form.save()
        return super().form_valid(form)
    

class Updateview(UpdateView):
    # form_class=student_form
    model=demo_student  
    fields=['name',"rollno","city","phone_number"]
    success_url='/'

    def get_form(self):
        form=super().get_form()
        form.fields['name'].widget=forms.TextInput(attrs={'class':'form-control'})
        return form
    

class Deleteview(DeleteView):
    model=demo_student
    success_url='/create/'
    template_name='demo/delete.html'