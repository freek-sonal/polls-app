from django.forms import ModelForm
from django import forms
from .models import Question,Comments

class QuestionForm(forms.Form):
    question = forms.CharField(max_length=200,required=True,help_text="*")
    choice_1 = forms.CharField(max_length=200,required=True,help_text="*")
    choice_2 = forms.CharField(max_length=200,required=True,help_text="*")
    choice_3 = forms.CharField(max_length=200,required=False)
    choice_4 = forms.CharField(max_length=200,required=False)
    choice_5 = forms.CharField(max_length=200,required=False)
    choice_6 = forms.CharField(max_length=200,required=False)
    choice_7 = forms.CharField(max_length=200,required=False)
    choice_8 = forms.CharField(max_length=200,required=False)
    image= forms.ImageField(required=False)

class CommentForm(ModelForm):
    class Meta:
        model=Comments
        exclude=['auth','pub_date','question',]
