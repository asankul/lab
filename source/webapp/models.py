from django.db import models

CATEGORY_CHOICES = [('other', 'Разное'), ('cat_1', 'Категория 1'), ('cat_2', 'Категория 2'), ('cat_3', 'Категория 3')]


class Products(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Название')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=200, default='other', verbose_name='Категория')
    count = models.PositiveIntegerField(default=0, verbose_name='Остаток')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')

    def __str__(self):
        return "{}. {}".format(self.pk, self.name)
