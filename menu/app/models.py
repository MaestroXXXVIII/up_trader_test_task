from django.db import models


class MenuCategory(models.Model):

    title = models.CharField('Название', max_length=50)
    slug = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'категория меню'
        verbose_name_plural = 'категории меню'

    def __str__(self):
        return self.title


class MenuItem(models.Model):

    title = models.CharField('Название', max_length=50)
    url = models.CharField(max_length=255)
    parent = models.ForeignKey('self',
                               verbose_name='Родитель',
                               on_delete=models.SET_DEFAULT,
                               blank=True,
                               null=True,
                               default=0,
                               related_name='parent_menu')
    category = models.ForeignKey(MenuCategory,
                                 verbose_name='Категория',
                                 blank=False,
                                 null=False,
                                 related_name='category_menu',
                                 on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'пункт меню'
        verbose_name_plural = 'пункты меню'

    def __str__(self):
        return self.title
