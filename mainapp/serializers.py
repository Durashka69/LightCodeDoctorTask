from rest_framework import serializers, exceptions

from mainapp.models import User, Doctor, Nurse


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=12, write_only=True)
    r_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'r_password')

    def validate(self, attrs):
        password = attrs.get('password')
        r_password = attrs.get('r_password')
        if len(password) < 6:
            raise exceptions.ValidationError(
                {"error": "password is too short"})
        elif len(password) > 20:
            raise exceptions.ValidationError({"error": "password is too long"})
        elif password != r_password:
            raise exceptions.ValidationError(
                {"error": "passwords don`t match"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data.get('email'),
            username=validated_data.get('username')
        )
        user.set_password(validated_data.get('password'))
        user.save()

        return user


class NurseSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    doctor_name = serializers.ReadOnlyField(source='doctor.user.username')

    class Meta:
        model = Nurse
        fields = (
            'id', 'user', 'job_title', 'doctor', 'doctor_name'
        )

        extra_kwargs = {
            'doctor': {'write_only': True}
        }

class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    nurse = NurseSerializer(read_only=True, many=True)

    class Meta:
        model = Doctor
        fields = (
            'id', 'user', 'job_title', 'nurse'
        )
