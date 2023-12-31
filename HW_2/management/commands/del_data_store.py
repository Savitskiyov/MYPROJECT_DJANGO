from django.core.management import BaseCommand
from HW_2.models import Client, Product, Order


class Command(BaseCommand):
    help = 'Del all data in the store'

    def handle(self, *args, **kwargs):
        Client.objects.all().delete()
        Product.objects.all().delete()
        Order.objects.all().delete()
