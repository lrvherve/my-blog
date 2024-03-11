from django.conf import settings #add
from django.db import models
from django.utils import timezone #add

# Create your models here.
class Post(models.Model): #signifie que Post est un modèle Django. Comme ça, Django sait qu'il doit l'enregistrer dans la base de données.
    #our cela, nous allons avoir besoin de définir le type de chaque champ (Est-ce que c'est du texte? Un nombre ? Une date ? Une relation à un autre objet, comme un objet utilisateur par exemple ?)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #C'est un lien vers un autre modèle.
    title = models.CharField(max_length=200)#Cela nous permet de définir un champ texte avec un nombre limité de caractères.
    text = models.TextField() #Cela nous permet de définir un champ text sans limite de caractères. Parfait pour le contenu d'un blog post, non ?
    created_date = models.DateTimeField(default=timezone.now) #Définit que le champ en question est un horodatage (date et heure).
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): #Il s'agit de notre méthode publish
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title