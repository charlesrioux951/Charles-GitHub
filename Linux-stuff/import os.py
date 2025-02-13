import os

def search_file_by_name(directory, filename):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

# Example usage
directory_to_search = '/path/to/search'
file_to_find = 'example.txt'
result = search_file_by_name(directory_to_search, file_to_find)

if result:
    print(f'File found: {result}')
else:
    print('File not found')