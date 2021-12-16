# NukePluginManager

Plugin to Manage Nuke Plugins using json files without the need to touch any files like the init.py file 
for testing and using nuke plugins.

## Install
Just download/clone the PluginManager and add the following code to ```<user home directory>/.nuke/init.py```

```
import sys
pathToPluginManager = PATH_TO_THE_PLUGIN_MANAGER_FOLDER # example: 'C:/Documents/Nuke/PluginManager'
sys.path.append(pathToPluginManager)
import pluginManager

pluginManager.init(silent=False)
```

The silent flag can be used to print the path of the loaded plugin directories at startup (if set to False).

## Using
To add plugins just create a new json File (like the examples) in the plugin folder.

Example json file structure:

```
{
	"enable": true,
	"expessionEnvs" : [],
	"env": [
		{
			"<NAME_OF_PLUGIN>": "<PATH_TO_PLUGIN>"
		}
		],
	"plugin_path": "$<NAME_OF_PLUGIN>"
}
```

The parsers adds all environment variables env to the environement Variables and adds the plugin (folder) at the plugin_path location.

All keys are optional.


| Json Keys  | description |
| --- | --- |
| enable  | (boolean/string) Flag if the plugin should be enabled. Can be a simple expression like: nuke.NUKE_VERSION_MAJOR==13 |
| expessionEnvs | (string) Python expresion which will be evaluated on runtime, eg. to determine the nuke version used |
| env  | (list of dict with strings) Environment variables like the path to the plugin or multiple subpathes or other environment variables |
| plugin_path  | (string) The path to the plugin which should be appended to the nuke plugin pathes |

Note: A definition can be used to only add environment variables on start up. See: examplePlugins/env.json
