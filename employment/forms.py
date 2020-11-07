from django import forms
from . import models

WORK_CHOICE = (
    ('painters', 'painters'),
    ('carpenter', 'carpenter'),
    ('handloom worker', 'handloom worker'),
    ('labour', 'labour'),
)


class RegisterWorker(forms.ModelForm):
    name = forms.CharField(max_length=21, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your Name',
        'name': 'User name',
        'id': 'id_event_name',
    }))
    slug = forms.SlugField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Dont Enter Anythin here!',
        'name': 'slug',
        'id': 'id_slug',
    }))
    requirement_type = forms.CharField(
        label='Choose your field', widget=forms.RadioSelect(choices=WORK_CHOICE))
    other = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter type of work involved'
    }))
    dob = forms.DateField(widget=forms.DateInput(attrs={
        'class': 'form-control',
        'type': 'date',
    }))
    aadhar = forms.CharField(max_length=12, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Aadhar Number',
    }))
    is_employed = forms.BooleanField(required=False)

    class Meta:
        model = models.Worker
        fields = ['name', 'slug', 'dob',  'aadhar',
                  'requirement_type', 'other', 'is_employed']
