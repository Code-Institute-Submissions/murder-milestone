{"filter":false,"title":"models.py","tooltip":"/checkout/models.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":2,"column":26},"action":"remove","lines":["from django.db import models","","# Create your models here."],"id":2},{"start":{"row":0,"column":0},"end":{"row":26,"column":65},"action":"insert","lines":["from django.db import models","from products.models import Product","","# Create your models here.","class Order(models.Model):","    full_name = models.CharField(max_length=50, blank=False)","    phone_number = models.CharField(max_length=20, blank=False)","    country = models.CharField(max_length=40, blank=False)","    postcode = models.CharField(max_length=20, blank=True)","    town_or_city = models.CharField(max_length=40, blank=False)","    street_address1 = models.CharField(max_length=40, blank=False)","    street_address2 = models.CharField(max_length=40, blank=False)","    county = models.CharField(max_length=40, blank=False)","    date = models.DateField()","","    def __str__(self):","        return \"{0}-{1}-{2}\".format(self.id, self.date, self.full_name)","","","class OrderLineItem(models.Model):","    order = models.ForeignKey(Order, null=False)","    product = models.ForeignKey(Product, null=False)","    quantity = models.IntegerField(blank=False)","","    def __str__(self):","        return \"{0} {1} @ {2}\".format(","            self.quantity, self.product.name, self.product.price)"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":25,"column":38},"end":{"row":25,"column":38},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1586255114821,"hash":"811b7eed6df79aeb1b8329d2f300165697c93c11"}