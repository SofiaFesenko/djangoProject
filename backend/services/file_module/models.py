import os

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

import settings
from uuid import uuid4


def get_file_path(instance, filename):
    branch_expansion = filename.split('.')
    ext = branch_expansion[-1]
    return f'{instance.content_type.model}/{instance.object_id}/{uuid4()}.{ext}'


class File(models.Model):
    file = models.FileField(upload_to=get_file_path, verbose_name='File')
    object_id = models.PositiveIntegerField(null=True, db_index=True, verbose_name='Object id')
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        null=True,
        db_index=True,
        verbose_name='Content type'
    )
    object = GenericForeignKey(for_concrete_model=False)

    class Meta:
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def delete(self, *args, **kwargs):
        try:
            os.remove(self.file.url[1:])
        except FileNotFoundError:
            pass

        super(File, self).delete(*args, **kwargs)

    @property
    def absolute_file_url(self):
        return f'{settings.SITE_URL}{self.file.url}'

    def __str__(self):
        return str(self.file)
