from django.contrib import admin
from django.conf.urls import url,include
from django.views.generic.base import TemplateView



urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='homepage.html'), name='home'),
    url('admin/', admin.site.urls),
    url('music/', include('music.urls')),


]
