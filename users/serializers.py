from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Add custom user data
        data.update({
            "first_name": self.user.first_name,
            "last_name": self.user.last_name,
            "access_level": self.user.access_level,
            "jwt_access": data.pop("access"),
            "jwt_refresh": data.pop("refresh"),
        })

        return data