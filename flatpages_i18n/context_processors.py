import settings


def flatpage_language_prefix(request):
    from django.utils import translation
    return {
        'FLATPAGE_LANGUAGE_PREFIX': '' if settings.LANGUAGE_CODE == translation.get_language() else '/' + translation.get_language()
    }
