from django.db import models


class Pill(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='../media')
    QR_AI01 = models.CharField(max_length=100)
    desc = models.TextField(max_length=10000)

    def __str__(self):
        return self.title


class Product(models.Model):
    pill = models.ForeignKey(Pill, on_delete=models.CASCADE)
    price = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return "%s - %s" % (self.pill.title, self.price)


class Pharmacy(models.Model):
    name = models.CharField(max_length=100)
    rating = models.FloatField()
    pills = models.ManyToManyField(Pill, related_name='pharmacies')
    products = models.ManyToManyField(Product)
    addr = models.TextField(max_length=10000)

    def __str__(self):
        return self.name
