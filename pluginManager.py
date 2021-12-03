import json
import os

import nuke

def init():
    managerDirectory = os.path.dirname(__file__)
    plugins = os.listdir(os.path.join(managerDirectory, "plugins"))
    for plugin in plugins:
        if plugin.endswith(".json"):
            with open(os.path.join(managerDirectory, "plugins", plugin)) as json_file:
                data = json.load(json_file)
                if "env" in data:
                    for item in data["env"]:
                        for key in item:
                            os.environ[key]=item[key]
                if "plugin_path" in data:
                    nuke.pluginAddPath(os.path.expandvars(data["plugin_path"]))
                    print("Loaded Plugin: {}".format(os.path.expandvars(data["plugin_path"])))
