from rest_framework.routers import DefaultRouter

from mainapp.views import(
    UserViewSet, DoctorViewSet, NurseViewSet
)


router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('doctors', DoctorViewSet, basename='doctors')
router.register('nurses', NurseViewSet, basename='nurses')

urlpatterns = []

urlpatterns += router.urls
