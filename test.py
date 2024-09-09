import ctypes

Dsparser_lib = ctypes.CDLL("./ds_parser_x86_64.so")
Dsparser_lib.parse_ds.restype = ctypes.c_char_p

input_file_path = "/Users/hyeonlee/Desktop/ACL/pythonGUI/DS Parser/ds00000000.tlm"

def parse_ds():
    output_file_path = Dsparser_lib.parse_ds(input_file_path.encode('utf-8'))
    print(f"output : {output_file_path.decode('utf-8')}")
    
parse_ds()
    