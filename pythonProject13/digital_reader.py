file_path = 'peter docs/jarvis/python/digital_library_assignment.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())