from django.conf import settings as dj_settings

from .apps import IamheadlessTranslateConfig
from .loader import load


class Settings:

    _TRANSLATION_REGISTRY = None

    APP_NAME = IamheadlessTranslateConfig.name
    VAR_PREFIX = APP_NAME.upper()

    VAR_TRANSLATION_REGISTRY_CLASS = f'{VAR_PREFIX}_TRANSLATION_REGISTRY_CLASS'

    @property
    def TRANSLATION_REGISTRY_CLASS(self):
        return getattr(
            dj_settings,
            self.VAR_TRANSLATION_REGISTRY_CLASS,
            'iamheadless_publisher_translate.registry.TransaltionRegistry'
        )

    @property
    def TRANSLATION_REGISTRY(self):
        if self._TRANSLATION_REGISTRY is not None:
            return self._TRANSLATION_REGISTRY
        self._TRANSLATION_REGISTRY = load(self.TRANSLATION_REGISTRY_CLASS)()
        return self._TRANSLATION_REGISTRY

    def __getattr__(self, name):
        return getattr(dj_settings, name)


settings = Settings()
