from django.utils import timezone

from submission.models import Article, STAGE_PUBLISHED

def yield_homepage_element_context(request, homepage_elements):
    if (
        homepage_elements is not None
        and homepage_elements.filter(name="Simple Carousel").exists()
    ):
        return {"carousel_items": request.journal.simple_carousel.simplecarouselslide_set.all()}
    else:
        return {}
