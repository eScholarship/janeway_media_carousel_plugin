from django import forms
from django.forms import BaseInlineFormSet, inlineformset_factory

from .models import SimpleCarousel, SimpleCarouselSlide
from cms.models import MediaFile

class SimpleCarouselSlideForm(forms.ModelForm):
    class Meta:
        model = SimpleCarouselSlide
        fields = ["header", "image", "text", "order"]
        widgets = {
            "text": forms.Textarea(attrs={"rows": 3}),
            "order": forms.NumberInput(attrs={"min": 0}),
        }

    def __init__(self, *args, **kwargs):
        journal = kwargs.pop("journal")
        super().__init__(*args, **kwargs)
        self.fields["order"].required = False
        self.fields["order"].help_text = "Leave blank to add at the end."
        self.fields["image"].queryset = MediaFile.objects.filter(journal=journal)


class BaseSimpleCarouselSlideFormSet(BaseInlineFormSet):
    """Slides shown in display order; new slides with no order go to the end."""

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("queryset", SimpleCarouselSlide.objects.order_by("order", "pk"))
        super().__init__(*args, **kwargs)

    def _next_order(self):
        if not hasattr(self, "_order_counter"):
            existing = [
                f.instance.order for f in self.initial_forms if f.instance.order is not None
            ]
            self._order_counter = max(existing, default=-1) + 1
        value = self._order_counter
        self._order_counter += 1
        return value

    def save_new(self, form, commit=True):
        obj = super().save_new(form, commit=False)
        if obj.order is None:
            obj.order = self._next_order()
        if commit:
            obj.save()
        return obj


SimpleCarouselSlideFormSet = inlineformset_factory(
    SimpleCarousel,
    SimpleCarouselSlide,
    form=SimpleCarouselSlideForm,
    formset=BaseSimpleCarouselSlideFormSet,
    extra=1,
    can_delete=True,
)
