from django.db import models

# Create your models here.

class Coupon_List(models.Model):

    company = models.CharField(max_length = 100)
    code = models.CharField(max_length = 200)
    expiry = models.DateTimeField()
    description = models.CharField(max_length = 500)
    used = models.BooleanField()

    #remove entry if used flag is true or if past expiry date

    class Meta:
        db_table = "coupon_list"

