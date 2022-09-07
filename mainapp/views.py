from rest_framework.viewsets import ModelViewSet

from mainapp.models import User, Doctor, Nurse
from mainapp.serializers import( 
    UserSerializer, DoctorSerializer, NurseSerializer
)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class NurseViewSet(ModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
