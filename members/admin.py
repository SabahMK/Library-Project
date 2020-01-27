from django.contrib import admin
from .models import Member,Rented_books
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin



class MemberInline(admin.StackedInline):
    model =Member 
    extra= 1
    max_num =1
    min_num = 1


class Rented_booksInline(admin.TabularInline):
    model = Rented_books
    extra= 1


class MemberAdmin(UserAdmin):
    inlines = (MemberInline,Rented_booksInline)

def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(MemberAdmin, self).get_inline_instances(request, obj)
# Register your models here.
admin.site.unregister(User)
admin.site.register(User, MemberAdmin)
