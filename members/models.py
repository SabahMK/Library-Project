from django.db import models
from books.models import Book
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class Member(models.Model):
    #name = models.CharField(_("Member_name"), max_length=50)
    user = models.ForeignKey(User, verbose_name =_("user"),related_name='profile', on_delete=models.CASCADE,blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    gender = models.CharField(_("Gender"),choices=(('male', 'Male'),('female','Female')), max_length=50)
    phone = models.CharField(_("Phone"), max_length=50)
    #email= models.EmailField(_("email"), max_length=254)
    state= models.CharField(_("State"), max_length=50)
    district = models.CharField(_("District"), max_length=50)
    languages = models.CharField(_("Languages"), max_length=50)
    occupation = models.CharField(_("Occupation"), max_length=50)


class Rented_books(models.Model):
    #name = models.CharField(_("Member_name"), max_length=50)
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name=_("book"),related_name="renter", on_delete=models.CASCADE)
    date = models.DateField(_("Rented on"), auto_now=False, auto_now_add=False)
    