from django.db.utils import OperationalError
from django.contrib.contenttypes.models import ContentType

from utils.models import Plugin


PLUGIN_NAME = 'Simple Carousel Plugin'
DISPLAY_NAME = 'Simple Carousel'
DESCRIPTION = 'Homepage element for a carousel similar to those in escholarship'
AUTHOR = 'Esther Verreau'
VERSION = '0.1'
SHORT_NAME = 'simple_carousel'
JANEWAY_VERSION = "1.8.0"


def install():
    import core.models as core_models
    import journal.models as journal_models

    plugin, created = Plugin.objects.get_or_create(
        name=SHORT_NAME,
        defaults={
            "enabled": True,
            "version": VERSION,
            "display_name": DISPLAY_NAME,
        }
    )


    # check whether this homepage element has already been installed for all journals
    journals = journal_models.Journal.objects.all()

    for journal in journals:
        content_type = ContentType.objects.get_for_model(journal)
        element, created = core_models.HomepageElement.objects.get_or_create(
            name=DISPLAY_NAME,
            template_path="simple_carousel/simple_carousel.html",
            content_type=content_type,
            object_id=journal.pk,
            has_config=True,
            configure_url="simple_carousel_config",
        )
        element.save()



def hook_registry():
    try:
        install()
        return {
            "yield_homepage_element_context": {
                "module": "plugins.simple_carousel.hooks",
                "function": "yield_homepage_element_context",
                "name": DISPLAY_NAME,
            }
        }
    except OperationalError:
        # if we get here the database hasn't yet been created
        return {}
    except BaseException:
        return {}
