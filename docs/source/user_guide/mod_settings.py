import json

settings_file = 'pytornado/settings/template.json'

with open(settings_file, 'r') as fp:
    settings = json.load(fp)

settings['plot']['show'] = False
settings['plot']['save'] = True

with open(settings_file, 'w') as fp:
    json.dump(settings, fp)