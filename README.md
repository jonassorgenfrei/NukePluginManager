# NukePluginManager

Plugin to Manage Nuke Plugins using json files without the need to touch any files like the init.py file 
for testing and using nuke plugins.


Just download/clone the PluginManager and add the following code to ```<user home directory>/.nuke/init.py```

```
import sys
pathToPluginManager = PATH_TO_THE_PLUGIN_MANAGER_FOLDER # example: 'C:/Documents/Nuke/PluginManager'
sys.path.append(pathToPluginManager)
import pluginManager

pluginManager.init(silent=False)
```

The silent flag can be used to print the path of the loaded plugin directories at startup (if set to False).

To add plugins just create a new additional json File (like the examples) in the plugin folder.
The json files needs the following structure:

```
{
	"env": [
		{
			"<NAME_OF_PLUGIN>": "<PATH_TO_PLUGIN>"
		}
		],
	"plugin_path": "$<NAME_OF_PLUGIN>"
}
```

The parsers adds all environment variables env to the environement Variables and adds the plugin (folder) at the plugin_path location.
