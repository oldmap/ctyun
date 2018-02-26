from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from dns.models import Domain, Record
from dns.serializers import DomainSerializer, RecordSerializer
from django.shortcuts import render


class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


@login_required
def index(request):
    records = Record.objects.all()
    return render(request, 'dns/index.html', {'records': records})

