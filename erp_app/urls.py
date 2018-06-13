
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from rest_framework import routers
from rest_framework.authtoken import views
# Users Structure - Views
from auth_users.views import AuthUserModelViewSet, GroupModelViewSet

# Menus Structure - Views
from modules.views import ModuleModelViewSet
from menus.views import MenuModelViewSet
from submenus.views import SubMenuModelViewSet 

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', AuthUserModelViewSet, base_name='users')
router.register(r'groups', GroupModelViewSet, base_name='groups')

# Menu Structure - Router
router.register(r'modules', ModuleModelViewSet, base_name='modules')
router.register(r'menus', MenuModelViewSet, base_name='menus')
router.register(r'submenus', SubMenuModelViewSet, base_name='submenus')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
