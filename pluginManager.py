import json
import os

import nuke

def init(silent=True):
    """
    Initializes the Plugin Manager and loads the plugin pathes defined by the json files in plugins.

    Args:
        silent (bool, optional): Flag to print the loaded Plugin pathes on start up. Defaults to True.
    """
    managerDirectory = os.path.dirname(__file__)
    plugins = os.listdir(os.path.join(managerDirectory, "plugins"))

    for plugin in plugins:
        if plugin.endswith(".json"):
            definitionFile = os.path.join(managerDirectory, "plugins", plugin)
            with open(definitionFile) as json_file:
                try:
                    data = json.load(json_file)

                    # pre checks 

                    # enable / disable plugin flag
                    if "enable" in data:
                        enableExpr = data["enable"]
                        enableExprType = type(data["enable"])
                        
                        if enableExprType is bool:
                            if not enableExpr:
                                continue
                        elif enableExprType is str:
                            # evaluate expressions
                            if not eval(enableExpr):
                                continue

                    # load data 

                    # append environment variables
                    if "env" in data:
                        for item in data["env"]:
                            for key in item:
                                os.environ[key]=os.path.expandvars(item[key])

                    # append plugin pathes
                    if "plugin_path" in data:
                        pluginPath = os.path.expandvars(data["plugin_path"])
                        
                        if os.path.exists(pluginPath):
                            # check if plugin path exists
                            nuke.pluginAddPath(pluginPath)
                            if not silent:
                                print("Loaded Plugin: {}".format(pluginPath))
                        else:
                            print("Error: Can't load Plugin: {}".format(pluginPath))

                except json.decoder.JSONDecodeError as e:
                    print("Can't load Plugin-Definition: {}".format(definitionFile))