import libtorrent as lt
import libtorrent

ses = lt.session()
ses.listen_on(6881, 6891)
params = { 'save_path': '.'} # useless
magnet_torrent = "./ok.torrent" # I should use the handle.name() function

link = "magnet:?xt=urn:btih:597A92F6EEED29E6028B70B416C847E51BA76C38&dn=ubuntu-13.10-desktop-i386.iso&tr=http%3a%2f%2ftorrent.ubuntu.com%3a6969%2fannounce&tr=http%3a%2f%2fipv6.torrent.ubuntu.com%3a6969%2fannounce"

handle = lt.add_magnet_uri(ses, link, params)


import time
print 'downloading metadata...'
while (not handle.has_metadata()): time.sleep(1)
print 'got metadata, starting torrent download...'
if handle.has_metadata():

    torinfo = handle.get_torrent_info()

    fs = libtorrent.file_storage()
    for file in torinfo.files():
        fs.add_file(file)

    torfile = libtorrent.create_torrent(fs)
    torfile.set_comment(torinfo.comment())
    torfile.set_creator(torinfo.creator())

    for i in xrange(0, torinfo.num_pieces()):
        hash = torinfo.hash_for_piece(i)
        torfile.set_hash(i, hash)

    for node in torinfo.nodes():
        torfile.add_node(node)
    
    # this line has issues, on utorrent it creates all files with same tier
    tier = 0
    for tracker in torinfo.trackers():
        torfile.add_tracker(tracker.url, tier)
        tier = tier + 1

    torfile.set_priv(torinfo.priv())

    f = open(magnet_torrent, "wb")
    f.write(libtorrent.bencode(torfile.generate()))
    f.close()

else:
	print 'no data'
