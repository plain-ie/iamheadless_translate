from .conf import settings

registry = settings.TRANSLATION_REGISTRY


def translate(key, language):
    return registry.translate(key, language)


def register(key, language, translation):
    return registry.register(key, language, translation)
