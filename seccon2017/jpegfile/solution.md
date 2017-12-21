write up ### JPEG File

The image is of a grey rectangle.  As the image opens withot errors and doesnt look corrupt it seems likely that it is a data section not dispalying.

Looking at the jpeg spec each marker is prefixed with 0xFF and when there is a 0xFF in the data segment it needs to be followed with 0x00.

https://en.wikipedia.org/wiki/JPEG#Syntax_and_structure

Using a hex editor I searched for all instances of 0xFF and checked that the following byte was either a correct jpeg marker or 0x00.

At offset 0x26f there is a marker that is 0xFC which is not valid.

The previous marker is a 'Start of Scan' (0xDA) and the one following is a piece of data (0x00) so this look like it should be data aswell.

Changing the byte 0xFC to 0x00 and saving the file makes the flag visible.

