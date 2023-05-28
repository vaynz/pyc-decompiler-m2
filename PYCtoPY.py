import uncompyle6.main as uncompyle

def decompile_pyc(pyc_file_path, output_file_path):
    with open(output_file_path, 'w') as output_file:
        uncompyle.decompile_file(pyc_file_path, output_file)

# Uncompile // choose path and directory
pyc_file_path = 'ConfigParser.pyc'
output_file_path = 'ConfigParser.py'
decompile_pyc(pyc_file_path, output_file_path)
