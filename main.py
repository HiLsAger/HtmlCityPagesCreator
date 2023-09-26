import os
import json
from cities import getCities

if __name__ == '__main__':
    root_directory = os.path.dirname(__file__)
    config = None
    with open("config.json") as file:
        file_content = file.read()
        config = json.loads(file_content)

    template = root_directory+config["template"]
    path = root_directory+config["path"]
    cities = getCities()

    with open(template, 'r') as file:
        template_content = file.read()

    for dir_name, city_name in cities.items():
        os.makedirs(os.path.join(path, dir_name), exist_ok=True)

        with open(os.path.join(path, dir_name, 'index.html'), 'w') as file:
            file.write(template_content.replace('<city>', 'г.' + city_name))
