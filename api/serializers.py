from rest_framework import serializers


class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=255)
    message = serializers.CharField()
    recipient_email = serializers.EmailField()
    recipient_name = serializers.CharField(max_length=100, required=False)
