import zlib, base64, os

def obtain_file_path(file_name):
    current_dir = os.getcwd()
    file_path = os.path.join(current_dir, 'file_compression', 'data', file_name)
    return file_path

def compress(input_file, output_file, compression_level=9):

    output_file_path = obtain_file_path(output_file)

    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    try:
        with open(input_file, 'rb') as f:
            data = f.read()
        compressed_data = base64.b64encode(zlib.compress(data, compression_level))
        with open(output_file_path, 'wb') as f:
            f.write(compressed_data)
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def decompress(input_file, output_file):
    output_file_path = obtain_file_path(output_file)

    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

    try:
        with open(input_file, 'rb') as f:
            encoded_data = f.read()
        decompressed_data = zlib.decompress(base64.b64decode(encoded_data))
        with open(output_file_path, 'wb') as f:
            f.write(decompressed_data)
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
