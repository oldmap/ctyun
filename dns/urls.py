from django.conf.urls import url, include
from dns import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'domains', views.DomainViewSet)
router.register(r'records', views.RecordViewSet)
router.register(r'types', views.TypeViewSet)


urlpatterns = [
    url(r'api/', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'', views.index),
]