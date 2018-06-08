
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework import routers
from rest_framework.authtoken import views
from auth_users.views import AuthUserModelViewSet, GroupModelViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', AuthUserModelViewSet, base_name='users')
router.register(r'groups', GroupModelViewSet, base_name='groups')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token)
] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
