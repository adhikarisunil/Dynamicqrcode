from django.db import models
from model_utils.fields import StatusField
from model_utils import Choices


# Create your models here.

class Dynamicqrcode(models.Model):
    


    name = models.CharField(max_length=255)
    QR_CODE_TYPE = Choices('English', 'Nepali')
    qr_code_type = StatusField(choices_name='QR_CODE_TYPE')
    content = models.JSONField(max_length=255)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
      return self.title

