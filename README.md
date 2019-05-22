## Sample Project for [DAL](https://github.com/yourlabs/django-autocomplete-light) issue

superuser: admin/admin

When using DAL within [django-nested-admin](https://github.com/theatlantic/django-nested-admin/) NestedTabularInline/NestedStackedInline, and a new row is added using "Add more Button" DAL fails to forward fields.

Replicating the issue:
- python manage.py runserver
- visit [this](http://127.0.0.1:8000/admin/error/modelparent/add/)
- The 1st inline text works properly, if you select anything in would not be shown in the list as Self() is being forwarded.
- If you add a new one using 'Add another Model Inline', it fails to forward Self().

According to nested admin integration it replaces this [regex](https://github.com/theatlantic/django-nested-admin/blob/de440b1333eeb9bd85ca412d717d0e89652207e7/nested_admin/static/nested_admin/src/nested-admin/jquery.djangoformset.js#L290).

fix "dal-forward-conf-for-" to "dal-forward-conf-for_" to be matched in the regex.
