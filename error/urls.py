from django.urls import path
from .views import ModelInlineAutoComplete

app_name = "error"
urlpatterns = [
    path(
        'error-autocomplete/',
        ModelInlineAutoComplete.as_view(),
        name='error-autocomplete',
    ),
]
