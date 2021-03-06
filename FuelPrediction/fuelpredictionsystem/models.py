from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.core.validators import MaxValueValidator, MinValueValidator
# from django.db.models import IntegerField, Model
# Create your models here.



class UserProfile(models.Model):
	STATE = (('TX', 'Texas'),('OTHERS', 'Out of Texas'))
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	# user = models.ForeignKey(User, on_delete=models.CASCADE)
	fullname = models.CharField(max_length=100, default='')
	address = models.CharField(max_length=100, default='')
	city = models.CharField(max_length=20, default='')
	state = models.CharField(max_length=20, choices=STATE)
	zipcode = models.IntegerField(default=0)

	def __str__(self):
		return self.user.username


class PriceHistoryModule(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	gallons_requested = models.IntegerField()
	delivery_date = models.DateField()
	delivery_address = models.CharField(max_length=200)
	suggested_price = models.FloatField()
	total_due = models.FloatField()
	
	# def __str__(self):
	# 	return self.user.username



# def create_profile(sender, **kwargs):
# 	if kwargs['created']:
# 		user_profile = UserProfile.objects.create(user=kwargs['instance'])
# post_save.connect(create_profile, sender = User)


# STATE = (  
#     ('INSTATE', 'Texas'),
#     ('OUTSTATE', 'Other State'),
# )
# SEASON = (  
#     ('SUMM', 'Summer'),
#     ('REST', 'Rest Of The Season'),
# )


