from django.contrib import admin
from django.conf.urls import url,include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^', include('account.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^articles/', include('articles.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
