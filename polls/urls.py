from . import views
from django.urls import path
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.detailview, name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('search/',views.search , name='search'),
    path('signup/',views.signup, name='signup'),
    path('form/',views.new_poll, name='form'),
    path('yourPolls/',views.yourPolls, name='yourPolls'),
]
