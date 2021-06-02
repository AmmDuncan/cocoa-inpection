from django.db import models
from django.urls import reverse

# Create your models here.
class Manager(models.Model):
    name = models.CharField(max_length=100)
    after_and = models.CharField(max_length=300, blank=True)
    
    def __str__(self):
        return self.name

class Report(models.Model):
    ITEM_INSPECTED_CHOICES = (
        ('v', 'Vehicle'),
        ('m', 'Motor Bike')
    )

    DEED_STATUS_CHOICES = (
        ('', 'select...'),
        ('c', 'COMPLETED')
    )
    TAKING_BENEFIT_CHOICES = (
        (0, 'NO'),
        (1, 'YES')
        )

    date = models.DateField(auto_now=True)
    date_created = models.DateField(auto_now_add=True, blank=True, null=True)
    name = models.CharField(max_length=100, unique=True)
    loan_for = models.CharField(choices=ITEM_INSPECTED_CHOICES,
                                default='v',
                                max_length=5)
    item_inspected = models.CharField(choices=ITEM_INSPECTED_CHOICES,
                                      default='v',
                                      max_length=5)
    make = models.CharField(max_length=70)
    registration = models.CharField(max_length=30)
    chasis_number = models.CharField(max_length=17)
    insurance_policy_number = models.CharField(max_length=50)
    insurance_starting_date = models.DateField()
    insurance_expiry_date = models.DateField()
    cubic_capacity = models.IntegerField()
    road_worthiness_starting_date = models.DateField()
    road_worthiness_expiry_date = models.DateField()
    driving_license_number = models.CharField(max_length=30)
    driving_license_starting_date = models.DateField()
    driving_license_expiry_date = models.DateField(verbose_name="License Expiry/Renewal Date")
    deed_status = models.CharField('Deed of Assignment', 
                                   choices=DEED_STATUS_CHOICES,
                                   max_length=5)
    currently_receiving = models.IntegerField(choices=TAKING_BENEFIT_CHOICES, default=0)
    manager = models.ForeignKey(Manager, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('get_report', args=[str(self.id)])

    class Meta:
        ordering = ['-date']