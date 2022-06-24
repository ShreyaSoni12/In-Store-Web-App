from django.db import models

# Create your models here.
class CustInsert(models.Model):
    
    name=models.CharField(max_length=100)
    address=models.TextField()
    amount=models.PositiveIntegerField()
    item_type=models.CharField(max_length=10)
    description=models.TextField()
    loan_date=models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="loan"