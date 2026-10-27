from django.db import models

class SimpleCarousel(models.Model):
    journal = models.OneToOneField(
        "journal.Journal",
        related_name="simple_carousel",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"Simple Carousel for {self.journal}"

class SimpleCarouselSlide(models.Model):
    carousel = models.ForeignKey("SimpleCarousel", on_delete=models.CASCADE)
    header = models.CharField(max_length=255)
    image = models.ForeignKey("cms.MediaFile", null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()
    order = models.PositiveIntegerField()
