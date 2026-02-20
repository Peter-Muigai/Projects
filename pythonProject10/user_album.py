def make_album(name, title, number=None):
    """Return name of artist and album title."""
    music = {'artist': name, 'album': title}
    if number:
        music['number']= number
    return music
while True:
    print("\nEnter a musician and his album(You can include the number of songs)")
    print("(Enter 'q' to quit.)")
    a_name = input("Enter artists name: ")
    if a_name == 'q':
        break
    a_title = input("Enter the album title:")
    if a_title == 'q':
        break
    album_case = make_album(a_name, a_title)
    print(album_case)