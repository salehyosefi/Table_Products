from django.db import models

# Create your models here.

class TableProduct(models.Model):
    name = models.CharField(max_length=250, verbose_name='نام محصول')
    price = models.IntegerField(verbose_name='قیمت محصول')
    number = models.IntegerField(verbose_name='تعداد')
    description = models.CharField(max_length=250, verbose_name='توضیحات')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.name
