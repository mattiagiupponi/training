from django.db import models
from django.db.models.signals import pre_save, post_save
from geonode.base.models import ResourceBase
from geonode.layers.models import Dataset


class TestModel(models.Model):
    
    name = models.CharField(max_length=200, help_text="This is the name of our field")
    description = models.TextField()
    is_enabled = models.BooleanField(default=False)
    number = models.IntegerField()
    related = models.CharField(max_length=100, default="", null=True)
    resource = models.ForeignKey(ResourceBase, blank=False, null=True, on_delete=models.CASCADE, default=None)

    def __str__(self) -> str:
        return self.name


def pre_save_function(instance, *args, **kwargs):
    """
    This is our function
    """
    instance.description = f"Let's modify the description!: {instance.description}"

pre_save.connect(pre_save_function, sender=TestModel)


def post_save_dataset(instance, *args, **kwargs):
    '''
    This is called after a dataset is saved
    '''
    print(f"The resource have the following ID: {instance.id}")
    
post_save.connect(post_save_dataset, sender=Dataset)