from django.db import models

class MediaCarousel(models.Model):
    journal = models.OneToOneField(
        "journal.Journal",
        related_name="media_carousel",
        on_delete=models.CASCADE,
    )
    header = models.CharField(max_length=255)

    def __str__(self):
        return f"Media Carousel for {self.journal}"

class MediaCarouselSlide(models.Model):
    carousel = models.ForeignKey("MediaCarousel", on_delete=models.CASCADE)
    header = models.CharField(max_length=255)
    image = models.ForeignKey("cms.MediaFile", null=True, blank=True, on_delete=models.CASCADE)
    text = models.TextField()
    order = models.PositiveIntegerField()
