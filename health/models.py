from django.db import models

# Create your models here.
class Step(models.Model): #Fields
    value = models.DecimalField(max_digits=6, decimal_places=2)

    date_created = models.DateTimeField(auto_now_add=True)

#Methods
def __str__(self):
    return 'Step #{}'.format(self.id)