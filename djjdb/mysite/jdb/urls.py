from django.urls import path
from . import views

app_name = 'jdb'

urlpatterns = [
#   path('', views.IndexView.as_view(), name='index'),
#    path('<int:pk>/', views.DetailView.as_view(), name='details'),
#    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
#    path('<int:question_id>/vote/', views.vote, name='vote'),
#   path('testSD/', views.testSD, name='testSD'),
#    path('testSD/',  views.testSDView.as_view(), name='testSD'),
#    path('boot/',  views.testBootstrapSD, name='bootstrap'),
     path('', views.listDb, name='listdb'),
]
