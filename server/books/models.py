from django.db import models
from django.utils.translation import ugettext as _


class Division(models.Model):
    name = models.CharField(_("Division Name"), max_length=150)
    slug = models.SlugField(_("Slug"))

    def __str__(self):
        return self.name


class District(models.Model):
    division = models.ForeignKey(
        Division,
        verbose_name=_("Division"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    name = models.CharField(_("District Name"), max_length=150)
    slug = models.SlugField(_("Slug"))

    def __str__(self):
        return self.name


class Thana(models.Model):
    district = models.ForeignKey(
        District,
        verbose_name=_("Division"),
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    name = models.CharField(_("Thana Name"), max_length=150)
    slug = models.SlugField(_("Slug"))

    def __str__(self):
        return self.name