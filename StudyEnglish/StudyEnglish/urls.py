from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('blog/', include('blog.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('auth_user.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)