from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Driver)
admin.site.register(models.Client)
admin.site.register(models.Order)

# @admin.register(Driver)
# class DriverAdmin(admin.ModelAdmin):
#     list_display = '__all__'
#
#     def __str__(self):
#         return self.name
#
#
# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#     list_display = '__all__'
#
#     def __str__(self):
#         return self.name
#
#
# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = '__all__'
#
#     def __str__(self):
#         return self.id
