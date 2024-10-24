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
