from django.db import models


class Pack(models.Model):
    pack_name = models.CharField(max_length=100, unique=True)
    components = models.ManyToManyField("Component", through="PackComponent")

    def __str__(self):
        return self.pack_name


class Component(models.Model):
    component_name = models.CharField(max_length=100, unique=True)
    packs = models.ManyToManyField("Pack", through="PackComponent")

    def __str__(self):
        return self.component_name


class PackComponent(models.Model):
    component = models.ForeignKey(
        Component, 
        on_delete=models.CASCADE,
        related_name='packs_component'
    )
    pack = models.ForeignKey(
        Pack, 
        on_delete=models.CASCADE,
        related_name='components_for_pack'
    )
    amount = models.IntegerField()