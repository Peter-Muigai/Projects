def make_album(name, title, number=None):
    """Return name of artist and album title."""
    music = {'artist': name, 'album': title}
    if number:
        music['number']= number
    return music

musician = make_album('post malone', 'F-T', number=9)
print(musician)