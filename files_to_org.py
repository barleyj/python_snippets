import os

file_extensions = ['.java']
dirs = {}

def print_org_header(depth, file):
    print ('*' * (depth)) + ' ' + file

def print_directory(dir):
    current_dir = dirs
    for i, sub_dir  in enumerate(dir.split('/')):
        if not current_dir.has_key(sub_dir):
            current_dir[sub_dir] = {}
            print_org_header(i + 1, ' ' + sub_dir)
        current_dir = current_dir[sub_dir]

def print_files(files):
    for file in files:
        print_org_header(i + 2, file)

def sanitize_directory(dir, replacements):
    dir = dir
    for replacement in replacements:
        dir = dir.replace(replacement, '')
    return dir
            
def process_directory(source_dir, replacements):
    for dir, directories, files in (dir for dir in os.walk(source_dir) if 'test' not in dir[0]):
        files = [os.path.splitext(file)[0] for file in files if os.path.splitext(file)[1] in file_extensions]
        if len(files) > 0:
            dir = sanitize_directory(dir, replacements)
            print_directory(dir)
            print_files(files)

if __name__ == "__main__":
    source_dir = '/Users/jayson.barley/development/8_0/plugins/records-retention/'
    replacements = ['/src', '/java', '/com', '/jivesoftware', '/main', source_dir]
    process_directory(source_dir, replacements)
