# Ped: Python Ed
The "standard text editor" 'Ed', now in Python 3.6. WIP.

For more information about what is 'Ed', see [this page](https://en.wikipedia.org/wiki/Ed_(text_editor)).

## User guide
**WARNING**
Before using this program, make sure you are not modifying an important file! This editor is still in a very early version and if it crashes, it will lose all modifications made to the file.

To use this program, simply open the 'main.py' and the file to be opened, like this:
```
python bin/main.py <pathToFile>
```
Once the file is opened, a prompt will appear. This current version contains the following operations:
* Append: Appends text to the current address line. Example:
```
 > 2a
This is an appended line to the second line of the file, so it will show up in the third line.
.
 >
```
* Change: Allows you to change the text found in the current address line:
```
 > 2c
This is a changed line. It allows you to make small changes to a line.
.
 > 
```
* Delete: Removes the current line:
```
 > 2d
(The second line of the file is removed)
 > 
```
* Print: Prints the contents of the file.
```
 > p
This is the first line.
This is the second line
...
 > 
```
* Enumerate: Enumerates the contents of the file:
```
 > n
1 This is the first line.
2 This is the second line
...
 > 
```
* Quit: Quits the program and saves the changes.
```
 > q
(The file contents will be changed)
$ 
```
