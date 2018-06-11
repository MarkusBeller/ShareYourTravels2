from django.db import models
from django.db.models.signals import post_save

class Category(models.Model):
    class Meta:
        verbose_name_plural ='categories'
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Item(models.Model):

    countries = models.TextField(null=True, blank=True)
    name = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='media', blank=True)
    category = models.ForeignKey(
        'Category',
        on_delete=models.DO_NOTHING
    )



    def __str__(self):
        return self.name

 #   def create_item(sender, **kwargs):
  #      if kwargs['created']:
   #         item = Item.objects.create(item=kwargs['instance'])
#
 #   post_save.connect(create_item, sender='')

