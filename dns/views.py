from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from dns.models import Domain, Record
from dns.serializers import *
from django.shortcuts import render
from dns.forms import RecordForm


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class DomainViewSet(viewsets.ModelViewSet):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer


@login_required
def index(request):
    record_form_obj = RecordForm()
    return render(request, 'dns/index.html', {'record_form_obj': record_form_obj})

