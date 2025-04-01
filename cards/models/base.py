from django.db import models

class CreatedOnMixin(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class UpdatedOnMixin(models.Model):
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class DeletedOnMixin(models.Model):
    deleted_on = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
