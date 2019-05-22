from dal import autocomplete
from .models import Alphabet


# Create your views here.

class ModelInlineAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Alphabet
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return qs.objects.none()

        qs = qs.objects.all()

        selected = self.forwarded.get('self', None)
        if selected is not None:
            qs = qs.exclude(pk__in=selected)

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs
