from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(min_value=1, max_value=2000)
    is_broken = serializers.BooleanField()
    problem_description = serializers.CharField(allow_null=True, required=False)
