from django.urls import path
from .views import HomePage,IndexPage,AloqaPage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('index/', IndexPage.as_view(), name='index'),
    path('contact/', AloqaPage.as_view(), name='contact'),
]
