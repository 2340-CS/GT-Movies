from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', include('home.urls')),
     path('movies/', include('movies.urls')),
    path('admin/', admin.site.urls),
    path('', include('moviesapp.urls')),
    path('movies/', include('moviesshow.urls')),
]

urlpatterns += static(settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
