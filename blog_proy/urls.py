from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url('^', include('django.contrib.auth.urls')),
    url(r'^about/', TemplateView.as_view(template_name="about.html"),name='about'),

]