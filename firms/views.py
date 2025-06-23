from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import generics
from .models import Firm
from .serializers import FirmSerializer
from .filters import FirmFilterSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class FirmListView(generics.ListAPIView):
    serializer_class = FirmSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('parent_id', openapi.IN_QUERY, description="Filter by parent_id", type=openapi.TYPE_INTEGER),
        openapi.Parameter('area_id', openapi.IN_QUERY, description="Filter by area_id", type=openapi.TYPE_INTEGER),
        openapi.Parameter('city_id', openapi.IN_QUERY, description="Filter by city_id", type=openapi.TYPE_INTEGER),
        openapi.Parameter('comdir_id', openapi.IN_QUERY, description="Filter by comdir_id", type=openapi.TYPE_INTEGER),
        openapi.Parameter('curator_id', openapi.IN_QUERY, description="Filter by curator_id", type=openapi.TYPE_INTEGER),
        openapi.Parameter('chiefaccountant_id', openapi.IN_QUERY, description="Filter by chiefaccountant_id", type=openapi.TYPE_INTEGER),
        openapi.Parameter('regionaldir_id', openapi.IN_QUERY, description="Filter by regionaldir_id", type=openapi.TYPE_INTEGER),
        openapi.Parameter('technicaldir_id', openapi.IN_QUERY, description="Filter by technicaldir_id", type=openapi.TYPE_INTEGER),
        openapi.Parameter('group_id', openapi.IN_QUERY, description="Filter by group_id", type=openapi.TYPE_INTEGER),
        openapi.Parameter('status_id', openapi.IN_QUERY, description="Filter by status_id", type=openapi.TYPE_INTEGER),
        openapi.Parameter('firm_id', openapi.IN_QUERY, description="Filter by firm_id", type=openapi.TYPE_INTEGER),
    ],
    security=[{"Bearer": []}])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        filter_serializer = FirmFilterSerializer(data=self.request.query_params)
        filter_serializer.is_valid(raise_exception=True)

        filters = filter_serializer.validated_data
        queryset = Firm.objects.all()
        if filters:
            queryset = queryset.filter(**filters)
        return queryset