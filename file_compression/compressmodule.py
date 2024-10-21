import zlib, base64, os

def obtain_file_path(file_name):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'data', file_name)
    return file_path

def compress(input_file, output_file):
    input_file_path = obtain_file_path(input_file)
    output_file_path = obtain_file_path(output_file)

    data = open(input_file_path, 'r').read()
    data_bytes = bytes(data, 'utf-8')
    compressed_data = base64.b64encode(zlib.compress(data_bytes, 9)) 
    decoded_data = compressed_data.decode('utf-8')
    open(output_file_path, 'w').write(decoded_data)

def decompress(input_file, output_file):
    input_file_path = obtain_file_path(input_file)
    output_file_path = obtain_file_path(output_file)

    input_file_content = open(input_file_path, 'r').read()
    encoded_input_content = input_file_content.encode('utf-8')
    decompressed_input_content = zlib.decompress(base64.b64decode(encoded_input_content))
    decoded_input_content = decompressed_input_content.decode('utf-8')
    open(output_file_path, 'w').write(decoded_input_content)