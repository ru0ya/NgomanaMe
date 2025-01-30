from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from jenga.models import Category, Tutorial, Step, Material, Comment


class TutorialForm(forms.ModelForm):
    class Meta:
        model = Tutorial
        fields = [
                'title',
                'category',
                'introduction',
                'difficulty_level',
                'estimated_time',
                ]


class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = [
                'step_number',
                'title',
                'description',
                ]


class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = [
                'name',
                'quantity',
                'optional',
                'notes',
                ]



class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'vintage-input'})
        self.fields['email'].widget.attrs.update({'class': 'vintage-input'})
        self.fields['password1'].widget.attrs.update({'class': 'vintage-input'})
        self.fields['password2'].widget.attrs.update({'class': 'vintage-input'})
