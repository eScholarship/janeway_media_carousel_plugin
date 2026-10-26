from django.contrib import messages
from django.urls import reverse
from django.shortcuts import redirect, render
from plugins.simple_carousel.forms import SimpleCarouselSlideFormSet

from plugins.simple_carousel.models import SimpleCarousel
from security.decorators import editor_user_required


@editor_user_required
def settings_view(request):
    if request.POST and "cancel" in request.POST:
        return redirect(reverse("core_manager_index"))

    carousel, _ = SimpleCarousel.objects.get_or_create(journal=request.journal)

    if request.method == "POST":
        formset = SimpleCarouselSlideFormSet(request.POST, instance=carousel, form_kwargs={'journal': request.journal})
        if formset.is_valid():
            formset.save()
            messages.success(request, "Carousel slides saved.")
            return redirect("home_settings_index")
    else:
        formset = SimpleCarouselSlideFormSet(instance=carousel, form_kwargs={'journal': request.journal})

    return render(
        request,
        "simple_carousel/simple_carousel_setup.html",
        {"carousel": carousel, "formset": formset},
    )
