MODELS=r'''
from django.db import models

# Create your models here.


class Handler(models.Model):

    STATUS_CHOICES = (
        ('New', 'New'),
        ('Processing', 'Processing'),
        ('Finish', 'Finish'),
        ('Timeout', 'Timeout'),
        ('Failed', 'Failed'),
        ('Successful', 'Successful'),
    )

    name = models.CharField(max_length=255, blank=True, null=True)
    pid = models.CharField(max_length=255, blank=True, null=True)
    input_data = models.BinaryField(default='')
    output_data = models.BinaryField(default='')
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='NEW')
    dist_path = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    time_cost = models.CharField(max_length=255, blank=True, null=True)
    @property
    def input_display(self):
        data = self.input_data[:50]
        return data

    @property
    def output_display(self):
        data = self.output_data[:50]
        return data
'''



