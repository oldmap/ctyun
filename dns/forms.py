from django.forms import ModelForm
from dns.models import Record


class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ['host', 'domain', 'type', 'value', 'priority']
