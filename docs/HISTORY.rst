There's a frood who really knows where his towel is
---------------------------------------------------

1.0b3 (unreleased)
^^^^^^^^^^^^^^^^^^

- Code defensively for a context that may not have a local registry by
  creating a new local registry. 
  [davidjb]
- Temporary workaround for not inheriting site defaults for plone.app.theming
  settings.
  [davidjb]
- Fix issue preventing setting theme on virtual hosted sites and directories.
  [davidjb]
- Add translatable string for theme field description.
  [davidjb]


1.0b2 (2013-08-15)
^^^^^^^^^^^^^^^^^^

- Removes ```Template``` option from ```theme``` drop-down (closes 
  `#1`_) [marcosfromero]

- Allows to select ```No theme``` (new empty option) and effectively
  removes local diazo template (closes `#2`_) [marcosfromero]

- Fix i18n and add Spanish and Brazilian Portuguese translations. [hvelarde]

- Support for Plone 4.1 was removed. [hvelarde]

- Update package documentation. [hvelarde]


1.0b1 (2013-04-21)
^^^^^^^^^^^^^^^^^^^

- Initial release.

.. _`#1`: https://github.com/collective/collective.behavior.localdiazo/issues/1
.. _`#2`: https://github.com/collective/collective.behavior.localdiazo/issues/2
