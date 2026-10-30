from django.urls import re_path
from plugins.simple_carousel import views

urlpatterns = [
    re_path(r"^settings/$", views.settings_view, name="media_carousel_config"),
]
