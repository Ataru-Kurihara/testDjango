from django.urls import path

from .views import Projects, Project

app_name = 'polls'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    path('projects/', Projects.as_view(), name='projects'),
    path('projects/<int:id>', Project.as_view(), name='project_id')
    # path('projects/<int:id>', project_id.as_view(), name='projects_id')

]
