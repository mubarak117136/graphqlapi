from django.db import models
from django.utils.translation import ugettext as _


class Books(models.Model):
    title = models.CharField(_("Book Title"), max_length=250)
    desc = models.TextField(_("Book Description"))

    def __str__(self):
        return self.title