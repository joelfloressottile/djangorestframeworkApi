from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from operators.views import OperatorViewSet, WeaponViewSet, SkinViewSet, GadgetViewSet

router = DefaultRouter()
router.register(r'operators', OperatorViewSet, basename='operators')
router.register(r'weapons', WeaponViewSet)
router.register(r'gadgets', GadgetViewSet)
router.register(r'skins', SkinViewSet)


urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace="admin_honeypot")),
    path('secret-access/', admin.site.urls),
    path('api/', include(router.urls)),
]
