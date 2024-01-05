from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),

    path('home/', views.search_view, name='search'),
    path('company/<int:id>/', views.company_detail, name='company_detail'),
    path('example/', views.sentence_example, name='sentence_example'),


    path('template/', views.generate_sentence, name='generation'),
    path('template/get-settings/', views.get_settings, name='get_settings'),

    
]