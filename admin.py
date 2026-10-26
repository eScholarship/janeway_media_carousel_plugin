from django.contrib import admin
from .models import SimpleCarousel, SimpleCarouselSlide


class SimpleCarouselSlideInline(admin.TabularInline):
    model = SimpleCarouselSlide
    extra = 1
    ordering = ("order",)


@admin.register(SimpleCarousel)
class SimpleCarouselAdmin(admin.ModelAdmin):
    inlines = [SimpleCarouselSlideInline]
    list_display = ("journal",)
