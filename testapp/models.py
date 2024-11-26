from django.db import models
from testapp.utils import CURRENCY_LIST, COUNTRY_LIST, phone_regex


CURRENCY = [ (curr,curr) for curr in CURRENCY_LIST ]

COUNTRY = [ (ctry,ctry) for ctry in COUNTRY_LIST ]


class TestModel(models.Model):
    name = models.CharField(verbose_name='Name', max_length=100, null=False, blank=False)
    sold_currency = models.CharField(verbose_name='Sold Currency', max_length=50, null=False, blank=False, choices=CURRENCY)
    get_currency = models.CharField(verbose_name='Get Currency', max_length=50, null=False, blank=False, choices=CURRENCY)
    phone_number = models.CharField(verbose_name='Phone number' ,max_length=17, validators=[phone_regex], null=False, blank=False)
    location = models.CharField(verbose_name='Location', max_length=100, choices=COUNTRY, null=False, blank=False)


    def __str__(self) -> str:
        return str(self.name)
