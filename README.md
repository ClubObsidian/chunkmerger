# chunkmerger

Merges chunks from two different worlds into the same world. This is done by copying region files
that do not exist and moving missing chunks over to region files that exist already. These files should
be worlds with the same world seed.

This is written by using the nbt code from the [minecraft region fixer](https://github.com/Fenixin/Minecraft-Region-Fixer).
This code was tweaked to work with chunkmerger, imports were changed to load in from the current directory
and `get_chunk` returns none if a chunk does not exist.
