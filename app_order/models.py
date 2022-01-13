from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ('simple', 'Simple'),
    ('middle', 'Middle'),
    ('lux', 'Lux'),
)


class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name='name')
    location = models.CharField(max_length=250, verbose_name='location')
    destination = models.CharField(max_length=250, verbose_name='destination')
    tel_number = models.CharField(max_length=20, verbose_name='tel_number')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='simple')

    def __str__(self):
        return self.name


class Driver(models.Model):
    name = models.CharField(max_length=200, verbose_name='name')
    license_number = models.CharField(max_length=30)
    car_number = models.CharField(max_length=30, verbose_name='car_number')
    tel_number = models.CharField(max_length=20, verbose_name='tel_number')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='simple')

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(Client,
                               related_name='orders',
                               on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver,
                               related_name='orders',
                               on_delete=models.CASCADE)

    class statuses(models.TextChoices):
        created = 'Created',
        cancelled = 'Cancelled',
        accepted = 'Accepted',
        finished = 'Finished',

    status_of_order = models.CharField(max_length=20, choices=statuses.choices, default='Created')

    def __str__(self):
        return f'{self.id} : order, {self.client.name} : client and {self.driver.name} : driver'
