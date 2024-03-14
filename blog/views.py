from django.shortcuts import render

# Create your views here.
# C'est dans la vue que nous allons ranger toute la partie "logique" de notre application. C'est elle qui va se charger d'aller chercher les informations liées à notre modèleque nous venons de créer et de les passer à un template.

def post_list(request):
    return render(request, 'blog/post_list.html', {}) #une fonction (def) appelée post_list qui prend une request (requête) et qui va return (retourner) la valeur donnée par une autre fonction render qui va assembler notre template blog/post_list.html