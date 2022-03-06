class TransaltionRegistry:

    translations = {}
    app_translations = {}

    def __init__(self):
        pass

    def register(self, key, language, translation, app=None):

        if key not in self.translations.keys():
            self.translations[key] = {}

        self.translations[key][language] = translation

        if app is not None:

            if app not in self.app_translations.keys():
                self.app_translations[app] = []

            self.app_translations[app].append(key)

    def bulk_register(list_of_translations):
        for x in list_of_translations:
            self.register(*x)

    def translate(self, key, language):
        try:
            return self.translations[key][language]
        except KeyError:
            pass
        return key
