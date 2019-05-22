from django.contrib import admin
import nested_admin
from .forms import ModelInlineForm
from .models import ModelInline, ModelParent


# Register your models here.
class ModelInlineAdmin(nested_admin.NestedStackedInline):
    model = ModelInline
    form = ModelInlineForm
    extra = 1


@admin.register(ModelParent)
class ModelParentAdmin(nested_admin.NestedModelAdmin):
    model = ModelParent
    inlines = [ModelInlineAdmin]
