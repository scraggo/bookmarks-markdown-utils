import json


def get_json_config():
    # this should be removed from other code, only used internally here
    with open("../config.json", "r") as read_file:
        return json.load(read_file)


# cache config
config = get_json_config()


def get_config_path(key, subKey):
    # use this throughout codebase
    if key not in ['directories', 'filenames', 'markdownFormat']:
        message = 'Could not find key: {}\n    Check config.json in the root of your project.'.format(
            key)
        raise ValueError(message)
    global config
    if not config:
        config = get_json_config()
    value = config.get(key).get(subKey)
    if value:
        return value
    message = 'Could not find key: {} at \'{}\'.\n    Check config.json in the root of your project.'.format(
        subKey, key)
    raise ValueError(message)
