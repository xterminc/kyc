from django.forms import ModelForm
from .models import LiveStockDetail

class LiveStockDetailForm(ModelForm):
    """Livestock detai form """

    class Meta:
        model = LiveStockDetail
        exclude = ('created_at', 'updated_at',)
