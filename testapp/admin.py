from django.contrib import admin
from testapp.models import TestModel


@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'sold_currency', 'get_currency', 'phone_number', 'location']

