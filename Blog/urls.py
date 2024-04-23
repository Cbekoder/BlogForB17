from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
