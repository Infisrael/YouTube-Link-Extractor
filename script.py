import re

# Define a regular expression pattern to match YouTube video URLs
pattern = r'https://www\.youtube\.com/watch\?v=([a-zA-Z0-9_-]+)'

# Open and read the text file, replace file.txt with your file you want to extract the YouTube links from
with open('file.txt', 'r') as file:
    text = file.read()

# Find all matches of the pattern in the text
matches = re.findall(pattern, text)

# Construct and write the complete YouTube video URLs to a file
with open('output.txt', 'w') as output_file:
    for match in matches:
        video_url = f'https://www.youtube.com/watch?v={match}'
        output_file.write(video_url + '\n')
