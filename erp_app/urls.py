
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

from rest_framework import routers
from rest_framework.authtoken import views
# Employee Strcuture - Views 
from employees.views import EmployeeModelViewSet
from employee_types.views import EmployeeTypeModelViewSet
from employee_positions.views import EmployeePositionModelViewSet 
# Person Structure 
from persons.views import PersonModelViewSet
from identification_documents.views import IdentificationDocumentModelViewSet
from identification_document_types.views import IdentificationDocumentTypeModelViewSet
# Users Structure - Views
from auth_users.views import AuthUserModelViewSet, GroupModelViewSet
# Entity Structure - Views 
from entity_classes.views import EntityClassModelViewSet
from entity_types.views import EntityTypeModelViewSet
from entity_activities.views import EntityActivityModelViewSet
from entities.views import EntityModelViewSet
from headquarterses.views import HeadquartersModelViewSet
from area_types.views import AreaTypeModelViewSet
from areas.views import AreaModelViewSet
# Extra Info 
from contact_information.views import ContactInformationModelViewSet
from extra_information.views import ExtraInformationModelViewSet
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
# Person Structure IdentificationDocumentTypeModelViewSet
router.register(r'persons', PersonModelViewSet, base_name='persons')
router.register(r'identification-documents', IdentificationDocumentModelViewSet, base_name='identification_documents')
router.register(r'identification-document-types', IdentificationDocumentTypeModelViewSet, base_name='identification_document_types')
# Employee Structure 
router.register(r'employees', EmployeeModelViewSet, base_name='employees')
router.register(r'employee-positions', EmployeePositionModelViewSet, base_name='employee_positions')
router.register(r'employee-types', EmployeeTypeModelViewSet, base_name='employee_types')
# User Structure 
router.register(r'users', AuthUserModelViewSet, base_name='users')
#router.register(r'user-profiles', AuthUserProfileModelViewSet, base_name='user_profiles')
router.register(r'groups', GroupModelViewSet, base_name='groups')
# Entity Structure 
router.register(r'entity-classes', EntityClassModelViewSet, base_name='entity_classes')
router.register(r'entity-types', EntityTypeModelViewSet, base_name='entity_types')
router.register(r'entity-activities', EntityActivityModelViewSet, base_name='entity_activities')
router.register(r'entities', EntityModelViewSet, base_name='entities')
router.register(r'headquarterses', HeadquartersModelViewSet, base_name='headquarterses')
router.register(r'area-types', AreaTypeModelViewSet, base_name='area_types')
router.register(r'areas', AreaModelViewSet, base_name='areas')
# Extra Info 
router.register(r'extra-information', ExtraInformationModelViewSet, base_name='extra_info')
router.register(r'contact-information', ContactInformationModelViewSet, base_name='contact_info')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
