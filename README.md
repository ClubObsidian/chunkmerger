# chunkmerger

[![Build](https://github.com/ClubObsidian/chunkmerger/workflows/Build/badge.svg)](https://github.com/ClubObsidian/chunkmerger/actions)
[![License](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://opensource.org/licenses/gpl-3.0.html)

Merges chunks from two different worlds into the same world. This is done by copying region files
that do not exist and moving missing chunks over to region files that exist already. These worlds should
be worlds with the same world seed.

This is written by using the nbt code from the [minecraft region fixer](https://github.com/Fenixin/Minecraft-Region-Fixer).
This code was tweaked to work with chunkmerger, imports were changed to load in from the current directory
and `get_chunk` returns `None` if a chunk does not exist.

## Running

Put files that you want to merge into the other world in the `sourceworldname/region` folder.

Put files that you want to merge into in the `destinationworldname/region` folder.

Run by using `merger.py -s sourcefolder -d destinationfolder`, you will need Python 3.

## Warning

Run at your own risk and make sure to have backups.
