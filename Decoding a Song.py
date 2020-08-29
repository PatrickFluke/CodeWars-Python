def song_decoder(song):
    # I struggled with this until I stumbled upon that "Split" removes the whitespaces. 
    # I realize that it can be cut down to just the return line, but leaving it like 
    # this because this is how I originally, finally, solved it.
    decodedSong = " ".join(song.replace("WUB", " ").split())
    return decodedSong
