# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from django.utils.encoding import force_text, python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.multidb import RoutingOneToOneField

@python_2_unicode_compatible
class UserSettings(models.Model):
    user = RoutingOneToOneField(settings.AUTH_USER_MODEL, editable=False, related_name='djangocms_usersettings')
    language = models.CharField(_("Language"), max_length=10, choices=settings.LANGUAGES,
                                help_text=_("The language for the admin interface and toolbar"))
    clipboard = models.ForeignKey('cms.Placeholder', blank=True, null=True, editable=False)

    class Meta:
        verbose_name = _('user setting')
        verbose_name_plural = _('user settings')
        app_label = 'cms'

    def __str__(self):
        return force_text(self.user)

    def has_placeholder_change_permission(self, user):
        return True
