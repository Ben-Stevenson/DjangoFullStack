
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from topperApp import views

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^$', views.index, name = 'index'),
	url(r'^topperApp/', include('topperApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
