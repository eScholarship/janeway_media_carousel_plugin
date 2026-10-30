from django.contrib import admin
from .models import MediaCarousel, MediaCarouselSlide


class MediaCarouselSlideInline(admin.TabularInline):
    model = MediaCarouselSlide
    extra = 1
    ordering = ("order",)


@admin.register(MediaCarousel)
class MediaCarouselAdmin(admin.ModelAdmin):
    inlines = [MediaCarouselSlideInline]
    list_display = ("journal",)
