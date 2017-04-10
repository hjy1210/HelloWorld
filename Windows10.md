## Windows Media Player do not work

Use [VLC media player](http://www.videolan.org/vlc/index.html) as substitute of windows media player.

## File Explorer do not work

Create a new shortcut to explorer.exe as suggested by 
[Don_71570](http://www.tomshardware.com/forum/id-2898069/folders-file-explorer-open.html):
```
I encountered this problem and a fix that worked for me was to create a new shortcut on the desktop 
(right click on an empty part of the desktop).
Browse to c:\windows and click on "explorer" or "explorer.exe" and click on "OK".
Click "Next" and "Finish".
Right click on the new shortcut and select "Properties"
On the "Shortcut" tab, where it says Target, add " /?" (without the quotes) That is space slash questionmark.
Click on OK.
Double click on the shortcut to verify that it works.
Right click on the taskbar icon - it creates on when it is running - and select "Pin to taskbar" - 
if you would like it accessible from the taskbar.
```
