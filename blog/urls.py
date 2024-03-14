"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
#Nous venons d'importer la fonction path de Django ainsi que toutes les vues liées à notre application blog.
# Ce modèle d’URL correspond à une chaîne vide et le résolveur d'URL de Django ignore le nom de domaine (par exemple, http://127.0.0.1:8000/), soit la première partie de l'URL. Ce pattern va donc indiquer à Django d'afficher la vue views.post_list à un utilisateur de votre site web qui se rendrait à l'adresse "http://127.0.0.1:8000/".
urlpatterns = [
    path('', views.post_list, name='post_list'),#Comme vous pouvez le voir, nous assignons une vue appelée post_list à l'URL racine. La dernière partie, name='post_list', est le nom de l'URL qui sera utilisée afin d'identifier la vue.
    
]

