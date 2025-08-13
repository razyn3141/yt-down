def is_valid_url(url):
    # Function to validate if the provided URL is a valid YouTube URL
    return url.startswith("https://www.youtube.com/watch?v=") or url.startswith("https://youtu.be/")

def get_file_extension(file_path):
    # Function to get the file extension from a file path
    return file_path.split('.')[-1] if '.' in file_path else '' 

def is_compatible_format(file_extension):
    # Function to check if the file format is compatible with Adobe Premiere
    compatible_formats = ['mp4', 'mov', 'm4a']
    return file_extension in compatible_formats