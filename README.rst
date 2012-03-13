The Skyrim Vertex Color scripts are used to globally overwrite vertex colors for a mesh.

Requirements
------------

* `blender 2.59 or newer <http://www.blender.org/download/get-blender/>`_
* `pyffi 2.2.0 or newer <http://sourceforge.net/projects/pyffi/files/pyffi-py3k/>`_

Author Notes
------------

This script was made as a brute force mass conversion script for vertex colors.
It was created to fill a niché in NifSkope's vertex editing capabilitie.
It was also used as a test case for the PyFFI's alpha support for Skyrim.

As such the script is not intended to be very robust from the user error. 
The instructions provided are intentionally simple and no guarantee is given should the use deviate from them

Usage
-----
* Install Blender 2.5+ in the default location
* Install PyFFI 2.20+ 
* Install the script folder to the add-ons directory
* Enable the add-on in the User Preferences.
* A new panel will be enabled in the Scene Tab.
 
* 1: Load the desired Skyrim .nif file.
* 2: The script will update the color wheel with the first encountered color
* 3: Select a new color to replace all vertex color values
* 4: An automated name is generated, basefile + "_copy.nif", which you can change.
* 5: Save.