from clld.web.maps import ParameterMap, Map


class MeaningMap(ParameterMap):
    def get_options(self):
        return {
            'base_layer': 'Esri.WorldTerrain',
            'icon_size': 20,
            'max_zoom': 9,
        }


class LanguagesMap(Map):
    def get_options(self):
        return {
            'base_layer': 'Esri.WorldTerrain',
            'icon_size': 20,
            'max_zoom': 9,
        }


def includeme(config):
    config.register_map('parameter', MeaningMap)
    config.register_map('languages', LanguagesMap)