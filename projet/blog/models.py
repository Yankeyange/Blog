from django.db import models

# Crons tout nos modèles pour notre blog

class Topic(models.Model):
  name = models.CharField(max_length=100)
  first_name = models.CharField(max_length=100)
  text = models.TextField()
  # permet de stocker la date actuelle accompagner de l'heure excate
  created_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    name = self.name
    # pour mettre la première lettre du nom en majuscule
    self.name = self.name.capitalize()
    # et de renvoyer le nom capitalizer
    return self.name


class Entry(models.Model):
  # on cré une clé étrangère entre cette nouvelle classe et la class Topic
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="entries")
  text = models.TextField()
  created_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    # sa va renvoyer les 50 premiéres lettres même les espaces sont considerer comme des lettres
    # donc fait attention à ce que tu vas écrire 
    return f"{self.text[:50]}..."
