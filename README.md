Magnet to Torrent
=================

This python script will convert a magnet link input into a magnet link that will save the `.torrent` file to the configured directory.

Dependencies
============

* python2.7 (will support python3 in the future)
* python-libtorrent
* Connection to the Internet

The python-libtorrent is used to retrieve the torrent file from the magnet metadata.

On Windows python-libtorrent can be downloaded from http://code.google.com/p/libtorrent/downloads/detail?name=python-libtorrent-0.16.10.win32.msi

And on Ubuntu
`apt-get install python-libtorrent`
