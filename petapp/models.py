from django.db import models

# Create your models here.
class user_tbl(models.Model):
	username=models.CharField(max_length=50,default="")
	phoneno=models.CharField(max_length=50,default="")
	email=models.CharField(max_length=50,default="")
	password=models.CharField(max_length=50,default="")
	status=models.CharField(max_length=50,default="approved")

class shop_tbl(models.Model):
	shopname=models.CharField(max_length=50,default="")
	address=models.CharField(max_length=50,default="")
	phoneno=models.CharField(max_length=50,default="")
	email=models.CharField(max_length=50,default="")
	password=models.CharField(max_length=50,default="")

class pets_tbl(models.Model):
	category=models.CharField(max_length=50,default="")
	name=models.CharField(max_length=50,default="")
	gender=models.CharField(max_length=50,default="")
	age=models.CharField(max_length=50,default="")
	colour=models.CharField(max_length=50,default="")
	description=models.CharField(max_length=50,default="")
	quantity=models.CharField(max_length=50,default="10")
	price=models.CharField(max_length=50,default="")
	file=models.FileField(upload_to="pets")
	status=models.CharField(max_length=50,default="approved")

class cart_tbl(models.Model):
	userid=models.ForeignKey(user_tbl, on_delete=models.CASCADE)
	pid=models.ForeignKey(pets_tbl,on_delete=models.CASCADE,default="",null=True)
	quantity=models.CharField(max_length=100,default='')
	total=models.CharField(max_length=100,default='')
	unitprice=models.CharField(max_length=100,default='')
	date=models.CharField(max_length=100,default='')
	status=models.CharField(max_length=100,default='pending')





class admin_signup_tb(models.Model):
	firstname=models.CharField(max_length=50,default="")
	lastname=models.CharField(max_length=50,default="")
	email=models.CharField(max_length=50,default="")
	gender=models.CharField(max_length=50,default="")
	password=models.CharField(max_length=50,default="")
	hpassword=models.TextField(default="")
		

class payment_tb(models.Model):
	userid=models.ForeignKey(user_tbl, on_delete=models.CASCADE)
	amount=models.CharField(max_length=50,default="")
	status=models.CharField(max_length=50,default="")
	date=models.CharField(max_length=50,default="")