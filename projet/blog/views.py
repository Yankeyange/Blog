from django.shortcuts import render, redirect
from blog.models import Topic
from blog.forms import TopicForm, EntryForm


# notre home page
def home(request):
  return render(request, 'home.html')

# les éléments de ma page
def topics(request):
  topics = Topic.objects.all()
  context = {'topics':topics}
  return render(request, 'topics.html', context)

# pour afficher les éléments d'un élément
def topic(request, topic_id):
  topic = Topic.objects.get(id=topic_id)
  entries = topic.entries.all()
  context = {'topic':topic, 'entries': entries}
  return render(request, 'topic.html', context)

# page pour ajouter un nouveau sujet

def new_topic(request):

  if request.method != 'POST':
    form = TopicForm()
  
  else:
    form = TopicForm(data=request.POST)

    if form.is_valid():
      form.save()
      return redirect('topics')
  context = {'form':form}
  return render(request, 'new_topic.html', context)

# ajouter des éléments à un seu sujet

def new_entry(request, topic_id):
  topic = Topic.objects.get(id=topic_id)

  if request.method != "POST":
    form = EntryForm()
  else:
    form = EntryForm(data=request.POST)
    if form.is_valid():
      new_entry = form.save(commit=False)
      new_entry.topic = topic
      new_entry.save()
      return redirect("topic", topic_id=topic_id)
  context = {'topic': topic, 'form':form}
  return render(request, 'new_entry.html', context)

