from django.shortcuts import render, redirect
from blog.models import Topic, Entry
from blog.forms import TopicForm, EntryForm
from django.contrib.auth import authenticate, login, logout


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
  # je met ce élément parce que dans mon modèles j'ai signifie 
  # le related_name = "entries"
  entries = topic.entries.all()
  context = {'topic':topic, 'entries': entries}
  return render(request, 'topic.html', context)

# page pour ajouter un nouveau sujet

def new_topic(request):

  if request.method != 'POST':
    # form va iriter de TopicForm
    form = TopicForm()
  
  else:
    form = TopicForm(data=request.POST)

    if form.is_valid():
      # si le formulaire est valid on sauvegarde
      form.save()
      # et on retourne à topics
      return redirect('topics')
  context = {'form':form}
  return render(request, 'new_topic.html', context)

# ajouter des éléments à un seu sujet

def new_entry(request, topic_id):
  topic = Topic.objects.get(id=topic_id)

  if request.method != "POST":
    form = EntryForm()
  else:
    # permet d'accéder aux données envoyer par une requête post
    form = EntryForm(data=request.POST)
    if form.is_valid():
      new_entry = form.save(commit=False)
      new_entry.topic = topic
      new_entry.save()
      return redirect("topic", topic_id=topic_id)
  context = {'topic': topic, 'form':form}
  return render(request, 'new_entry.html', context)


# ou l'utilisateur pourra modifier ces entrées

def edit_entry(request, entry_id):
  """ on pourra modifier une entré existante"""
  entry = Entry.objects.get(id=entry_id)
  # on récupère le sujet topic de cette entitée
  topic = entry.topic

  if request.method !="POST":
    # cette partie signifie que j'initialise mon formulaire avec
    # l'instance entry déjà crée
    # cela permettra à l'utilisateur de faire les modifications
    form = EntryForm(instance=entry)

  else:
    form = EntryForm(instance=entry, data=request.POST)
    if form.is_valid():
      form.save()
      # cela permet de retourner l'utilisateur à la page de topic là
      # mais avec une action réussi 
      return redirect("topic", topic_id=topic.id)
    
  context = {'entry':entry, 'topic':topic, 'form':form}
  return render(request, 'edit_entry.html', context)

# login page 
def loginpage(request):
   if request.method =="POST":
        name=request.POST.get("username")
        pass1=request.POST.get("pass")
        print(name, pass1)

# logout page 
def logoutpage(request):
  pass

# registration page

def registration(request):
  pass