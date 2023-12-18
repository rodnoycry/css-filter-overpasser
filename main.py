import requests
import os
from files_map import FILES_MAP


url = "https://phl.spbu.ru/administrator/index.php?option=com_content&layout=edit&id=497"


def parse_headers(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    headers = {}
    current_key = None

    for line in lines:
        line = line.strip()
        if line.endswith(":"):
            current_key = line[:-1]
            headers[current_key] = ''
        elif current_key is not None:
            headers[current_key] += line

    # Remove any empty headers
    headers = {k: v for k, v in headers.items() if v.strip()}

    return headers

def parse_payload(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        payload_data = file.read()

    payload = {}
    for line in payload_data.split('\n'):
        key_value = line.split(': ', 1)
        if len(key_value) == 2:
            key, value = key_value
            payload[key] = value

    return payload

def modify_description(payload, file_path, is_article=True):
    content_key = 'jform[articletext]' if is_article else 'jform[content]'
    with open(file_path, 'r') as file:
        new_description = file.read()
        payload[content_key] = new_description
    return payload

def make_post_request(url, headers, payload):
    response = requests.post(url, headers=headers, data=payload)
    return response.status_code

def main(files_dict, token=None):
    headers_file_path = 'headers.txt'
    payload_file_path = files_dict['payload']
    update_file_path = convert_cyrillic_to_unicode(files_dict['html'])

    parsed_headers = parse_headers(headers_file_path)
    parsed_payload = parse_payload(payload_file_path)

    parsed_payload = modify_description(parsed_payload, update_file_path, is_article=True)
    if token:
        parsed_payload[token] = 1

    response_code = make_post_request(url, parsed_headers, parsed_payload)
    if response_code == 200:
        print(f"\n{str(response_code)}: '{'_'}' updated successfully (probably)\n")
    else:
        print(f"\n{str(response_code)}: '{'_'}' something went wrong on update\n")
    os.remove(update_file_path)


def convert_cyrillic_to_unicode(src_file_path):
    # Ensure the source file exists
    if not os.path.isfile(src_file_path):
        raise FileNotFoundError(f"The file {src_file_path} does not exist.")

    # Determine the directory and filename
    directory, filename = os.path.split(src_file_path)
    name, ext = os.path.splitext(filename)

    # Create a new filename for the output
    new_filename = f"{name}_converted{ext}"
    new_file_path = os.path.join(directory, new_filename)

    # Read the source file and convert Cyrillic characters to Unicode escape sequences
    with open(src_file_path, 'r', encoding='utf-8') as src_file:
        content = src_file.read()

    # Convert Cyrillic to Unicode escape sequences
    converted_content = ''.join([f"\\u{ord(char):04x}" if 0x0400 <= ord(char) <= 0x04FF or 0x0500 <= ord(char) <= 0x052F else char for char in content])

    # Write the converted content to the new file
    with open(new_file_path, 'w', encoding='utf-8') as new_file:
        new_file.write(converted_content)

    return new_file_path


if __name__ == "__main__":
    files_dict = FILES_MAP.js_css_applications
    token = ''
    main(files_dict, token)