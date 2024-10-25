from django.shortcuts import render
from blog.models import Topic

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
