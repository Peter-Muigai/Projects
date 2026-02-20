# A simple file reader .
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
            print(f"\n{contents}")
    except FileNotFoundError:
        print(f"Sorry, the file does not exist.")
    else:
        print(f"\nContents of {filename}:\n{contents}")