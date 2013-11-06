# -*- coding: utf-8 *-*

from zope.component import queryUtility
from zope.schema import getFields
from plone.registry.interfaces import IRegistry
from plone.app.theming.interfaces import IThemeSettings
from Products.Five import BrowserView
from plone.app.theming.utils import getAvailableThemes
from collective.behavior.localdiazo.behavior import DISABLE_PLONE_APP_THEMING


class LocalRegistrySetter(BrowserView):
    """ Utility view to set theme in the local registry,
        we need to work in a subrequest to get the local registry.
    """

    def __call__(self):
        """
        """
        registry = queryUtility(IRegistry)
        if registry != self.context.get('local_registry'):
            return
        settings = registry.forInterface(IThemeSettings, False)
        themes = getAvailableThemes()

        if self.context.theme:
            settings.enabled = self.context.theme != DISABLE_PLONE_APP_THEMING
            for theme in themes:
                if theme.rules == self.context.theme:
                    settings.currentTheme = theme.__name__.decode()
                    settings.rules = theme.rules
                    settings.absolutePrefix = theme.absolutePrefix
                    settings.parameterExpressions = theme.parameterExpressions
                    settings.doctype = theme.doctype
        else:
            return
            fields = getFields(IThemeSettings)
            settings_fields = ('currentTheme', 'rules', 'absolutePrefix', 'parameterExpressions', 'doctype',)
            for settings_field in settings_fields:
                setattr(settings, settings_field, fields[settings_field].default)
