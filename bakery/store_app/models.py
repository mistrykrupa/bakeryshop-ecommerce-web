from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import post_save
from django.dispatch import receiver
# from .models import UserProfile

from ckeditor.fields import RichTextField

from django.forms import ValidationError
#from django.utils import timezone
# Create your models here.
"""
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='Profile')
    image= models.ImageField(upload_to='Item_images/img', default='default.svg')
    phone = models.IntegerField(null=True)
    address=models.TextField(null=True)
    

    def __str__(self):
        return f'{self.user} Profile'
"""

class Categories(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def clean(self):
        existing_category = Categories.objects.filter(name=self.name)
        if self.pk:
            existing_category = existing_category.exclude(pk=self.pk)
        if existing_category.exists():
            raise ValidationError("Category with this name already exists.")


  
class Flavour(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Filter_Price(models.Model):
    FILTER_PRICE=(
        ('10 To 200','10 To 200'),
        ('200 To 500','200 To 500'),
        ('500 To 1000','500 To 1000'),
        ('1000 To 1500','1000 To 1500'),
        ('1500 To 2000','1500 To 2000'),
        ('2000 To 5000','2000 To 5000'),
    )    

    price=models.CharField(choices=FILTER_PRICE,max_length=60)

    def __str__(self):
        return self.price

class Item(models.Model):
    STOCK=('IN STOCK','IN STOCK'),('OUT OF STOCK','OUT OF STOCK')
    INGREDIENTS=('WITH EGG','WITH EGG'),('WITHOUT EGG','WITHOUT EGG')
    STATUS=('Publish','Publish'),('Draft','Draft')

    unique_id=models.CharField(unique=True,max_length=200,null=True,blank=True)
    image=models.ImageField(upload_to='Item_images/img')
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    information=RichTextField(null=True)
    description=RichTextField(null=True)
    stock=models.CharField(choices=STOCK,max_length=200)
    ingredients=models.CharField(choices=INGREDIENTS,max_length=200)
    status=models.CharField(choices=STATUS,max_length=200)  
    created_date=models.DateTimeField(default=timezone.now)


    categories=models.ForeignKey(Categories,on_delete=models.CASCADE)
    flavour=models.ForeignKey(Flavour, on_delete=models.CASCADE) 
    filter_price=models.ForeignKey(Filter_Price, on_delete=models.CASCADE)

    def clean(self):
        existing_item = Item.objects.filter(name=self.name)
        if self.pk:
            existing_item = existing_item.exclude(pk=self.pk)
        if existing_item.exists():
            raise ValidationError("Item with this name already exists.")


    

    def save(self,*args,**kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id=self.created_date.strftime('75%Y%m%d23') + str(self.id)
        return super().save(*args,**kwargs)   
    

    def __str__(self):
         return self.name
  


    

class Contact_us(models.Model):
    name = models.CharField(max_length=200)       
    email = models.EmailField(max_length=200)
    phone = models.IntegerField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email    


class Order(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)  
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField(null=True)
    address=models.TextField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pin=models.IntegerField() 
    #amount=models.IntegerField(null=True)
    amount=models.CharField(max_length=100,null=True)
    payment_id=models.CharField(max_length=200,null=True,blank=True)
    paid=models.BooleanField(default=False,null=True)
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    PROCESS = ('PENDING','PENDING'),('IN PROCESS','IN PROCESS'),('MADE','MADE')
    item=models.ForeignKey(Item,on_delete=models.CASCADE,null=True)
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    item=models.CharField(max_length=200)
    image=models.ImageField(upload_to='Item_images/img')
    quantity=models.CharField(max_length=20)
    price=models.CharField(max_length=50)
    process=models.CharField(choices=PROCESS,max_length=200,default='PENDING',null=False)
    total=models.CharField(max_length=100)

    def __str__(self):
        return self.item


class Review(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()  # Rating can be on a scale of 1-5
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.review


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.FloatField()
    valid_from = models.DateField()
    valid_to = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.IntegerField(null=False,default='0')
    address=models.TextField(max_length=200,null=False,default='')
    city=models.CharField(max_length=100,null=False,default='')
    state=models.CharField(max_length=100,null=False,default='')
    pin=models.IntegerField(default='0') 


    def _str_(self):
        return self.user.username

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # bio = models.TextField(max_length=500, blank=True)
    
    phone = models.CharField(max_length=12, blank=True)
    # birth_date = models.DateField(null=True, blank=True)
    address=models.CharField(max_length=12, blank=True)
    profile_image = models.ImageField(default='client1.jpg', upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()




class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    item=models.ForeignKey(Item,on_delete=models.CASCADE)




"""
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, related_name="profile")
    is_email_verified=models.BooleanField(default=False)
    email_token=models.CharField(max_length=100,null=True,blank=False)
    profile_image=models.ImageField(upload_to='Item_images/img',null=True)

    def get_cart_count(self):
        return request.session.cart|length

def get_file_path(instance,filename):
     return f"uploads/{filename}"
"""