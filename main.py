import requests
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

def main(target_css_id):
    files_dict = FILES_MAP[target_css_id]
    headers_file_path = 'headers.txt'
    payload_file_path = files_dict['payload']
    update_file_path = files_dict['html']

    parsed_headers = parse_headers(headers_file_path)
    parsed_payload = parse_payload(payload_file_path)

    parsed_payload = modify_description(parsed_payload, update_file_path, is_article=True)

    response_code = make_post_request(url, parsed_headers, parsed_payload)
    if response_code == 200:
        print(f"\n{str(response_code)}: '{target_css_id}' updated successfully\n")
    else:
        print(f"\n{str(response_code)}: '{target_css_id}' something went wrong on update\n")


if __name__ == "__main__":
    target_css_id = 'css-search-page'
    main(target_css_id)