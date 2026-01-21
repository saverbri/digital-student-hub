import random
import string

def generate_random_code(length=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

def format_file_size(size):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} TB"