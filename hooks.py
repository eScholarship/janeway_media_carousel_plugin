
def yield_homepage_element_context(request, homepage_elements):
    if (
        homepage_elements is not None
        and homepage_elements.filter(name="Media Carousel").exists()
    ):
        return {"carousel_items": request.journal.media_carousel.mediacarouselslide_set.all()}
    else:
        return {}
