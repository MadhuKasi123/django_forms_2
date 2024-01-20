from django import forms
from app.models import *


class TopicForm(forms.Form):
    topic_name=forms.CharField()

class WebpageForm(forms.Form):
    t1=[[to.topic_name,to.topic_name] for to in Topic.objects.all()]

    topic_name=forms.ChoiceField(choices=t1)
    name=forms.CharField()
    url=forms.URLField()
class AccessRecordsForm(forms.Form):
    wl=[[WO.pk,WO.name] for WO in Webpage.objects.all()]
    name=forms.ChoiceField(choices=wl)
    date=forms.DateField()
    author=forms.CharField()

