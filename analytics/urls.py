from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),

    path('search/', views.search_view, name='search'),
    path('company/<int:id>/', views.company_detail, name='company_detail'),
    path('sentenceexample/', views.sentence_example, name='sentence_example'),


    path('generation/', views.generate_sentence, name='generation'),
    path('generation/get-settings/', views.get_settings, name='get_settings'),

    
]