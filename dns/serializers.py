from dns.models import *
from rest_framework import serializers


class DomainSerializer(serializers.ModelSerializer):

    class Meta:
        model = Domain
        fields = '__all__'


class RecordSerializer(serializers.ModelSerializer):


    class Meta:
        model = Record
        fields = '__all__'
