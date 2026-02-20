favorite_languages = {
    'peter': 'python',
    'mark': 'java',
    'mike': 'c',
    'jane': 'ruby',
    'kim': 'html'
    }
print("The following languages were chosen:")
for language in sorted(favorite_languages.values()):
    print(language.title())
