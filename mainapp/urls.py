from os.path import abspath, basename, dirname

from django.urls import path

from .views import Index, Contact, About, Cats, Dogs, Volunteer, BlogHome, BlogSingle, Elements


app_name = basename(dirname(abspath(__file__)))

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('contact/', Contact.as_view(), name='contact'),
    path('about/', About.as_view(), name='about'),
    path('cats/', Cats.as_view(), name='cats'),
    path('dogs/', Dogs.as_view(), name='dogs'),
    path('volunteer/', Volunteer.as_view(), name='volunteer'),
    path('blog-home/', BlogHome.as_view(), name='blog-home'),
    path('blog-single/', BlogSingle.as_view(), name='blog-single'),
    path('elements/', Elements.as_view(), name='elements'),
]
