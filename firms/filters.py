from rest_framework import serializers

class FirmFilterSerializer(serializers.Serializer):
    parent_id = serializers.IntegerField(required=False)
    area_id = serializers.IntegerField(required=False)
    city_id = serializers.IntegerField(required=False)
    comdir_id = serializers.IntegerField(required=False)
    curator_id = serializers.IntegerField(required=False)
    chiefaccountant_id = serializers.IntegerField(required=False)
    regionaldir_id = serializers.IntegerField(required=False)
    technicaldir_id = serializers.IntegerField(required=False, allow_null=True)
    group_id = serializers.IntegerField(required=False)
    status_id = serializers.IntegerField(required=False)
    firm_id = serializers.IntegerField(required=False)