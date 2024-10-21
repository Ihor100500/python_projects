import os
import zlib, base64

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'data', 'demo.txt')
compressed_file_path = os.path.join(script_dir, 'data', 'compressed.txt')

data = open(file_path, 'r').read()
data_bytes = bytes(data, 'utf-8')
compressed_data = base64.b64encode(zlib.compress(data_bytes, 9)) 
decoded_data = compressed_data.decode('utf-8')
open(compressed_file_path, 'w').write(decoded_data)

decompressed_data = zlib.decompress(base64.b64decode(compressed_data))
print(decompressed_data)
