urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home.html),
    path('hello', views.hello.html),
    path("Nothig is happ")
]

'''
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    '''


from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home.html),
    path('hello', views.hello.html),
    path("Nothig is happ")
]
class Dreamreal(models.Model):

   website = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   website = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   name = models.CharField(max_length = 50)
   phonenumber = models.IntegerField()

   class Meta:
      db_table = "dreamreal"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home.html),
    path('hello', views.hello.html),
]


class Dreamreal(models.Model):
        
        
  class Dreamreal(models.Model):
   website = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   website = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   name = models.CharField(max_length = 50)
   phonenumber = models.IntegerField()

       
  class Dreamreal(models.Model):

   website = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   website = models.CharField(max_length = 50)
   mail = models.CharField(max_length = 50)
   name = models.CharField(max_length = 50)
   phonenumber = models.IntegerField()

   class Meta:
      db_table = "dreamreal"

