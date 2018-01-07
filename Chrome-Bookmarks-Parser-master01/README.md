# Chrome Bookmarks Parser

A pair of scripts that parses the Bookmarks.bak json and outputs it
as a compatible HTML file that Chrome can import again.

Originally written as a means of preventing complete bookmark loss in the rare instances that Chrome explodes (and it does). This can be scheduled to run on your system to keep a fresh backup as needed, or as a last-ditch effort when everything's already on fire.  

## Installation

Scripts rely on Python 3. No external libraries/modules needed.

## Usage

1. Navigate to the script's directory. 
2. Run `python Chrome_Bookmarks_backup.py` in Windows Command Prompt, Terminal, or whatever your system uses.
3. Backup script will perform its job and call `Chrome_Bookmarks_Parser.py` which will parse `Bookmarks.bak` and output an HTML file with your bookmarks.

## Contributing

As I don't have access to a system with any Linux distro or Mac OS X, I have written the Backup script according to what I could find online and my own knowledge. Testing of these is welcomed on the related systems along with fixes. 

## Credits

Credits to Matt Jones (mattCreative)'s PHP script which served 
as the framework for this one.
https://github.com/mattCreative/chrome-bookmarks-converter

## License

GNU GPL v3
