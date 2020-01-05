from django.urls import path
from django.conf.urls import url,include
from django.template import loader
from . import views
from django.views.generic.base import TemplateView

app_name = 'music'

urlpatterns = [
    #/music/
    path('',views.IndexView.as_view(), name = 'index'),
    #/music/71/
    path('<int:pk>/',views.DetailView.as_view(), name = 'detail'),
    # /music/album/add
    path('<album/add>/', views.AlbumCreate.as_view(), name='album-add'),
    # /music/accounts
    url('accounts/', include('accounts.urls')),
    # /music/accounts
    url('Utube/', TemplateView.as_view(template_name='YTindex.html'), name='utube'),


]
