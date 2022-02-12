from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from restapi.views import UserViewSet
from django.conf.urls.static import static
from django.conf import settings
import debug_toolbar

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('restapi.urls')),
    path('front/', include("front.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('__debug__/', include("debug_toolbar.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)