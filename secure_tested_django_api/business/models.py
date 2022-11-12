from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')




class Customer(models.Model):
    STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )


    GENDER_CHOICES =(
        ('MALE','MALE'),
        ('FEMALE','FEMALE'),
        ('INTERSEX','INTERSEX')
    )
    AMOUNT_CHOICES =(
        ('Success','Success'),
        ('Cancel','Cancel'),
        ('Pending','Pending')
    )



    title=models.CharField(max_length=250)
    name=models.CharField(max_length=250)
    last_name=models.CharField(max_length=250)
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    email=models.EmailField(max_length=20) 
    password=models.CharField(max_length=10)
    amount=models.CharField(max_length=20,choices=AMOUNT_CHOICES)
    
    created_by=models.ForeignKey(User, related_name='created_by',  editable=False, on_delete=models.PROTECT, default=1)
    created = models.DateTimeField(default=timezone.now)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    def __str__(self):
        return "{} {}".format(self.name,self.last_name)