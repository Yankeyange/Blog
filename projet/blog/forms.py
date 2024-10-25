from django import forms
from blog.models import Topic, Entry

class TopicForm(forms.ModelForm):
  class Meta:
    model = Topic
    fields = ['name','first_name', 'text']

class EntryForm(forms.ModelForm):
  class Meta:
    model = Entry
    fields = ['text',]