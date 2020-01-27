import os
import subprocess

def write_files(import_filename, raw_data, dest_dir, file_info):
    for index, info in enumerate(file_info):
        offset = info.start_offset
        end_offset = info.end_offset
        filename = info.filename
        if (info.compression_type == "none"):
            with open(dest_dir + "/" + filename, "wb") as shapeFile:
                print("extracting " + dest_dir + "/" + filename + ", compression type:", info.compression_type)
                new_file_byte_array = bytearray(raw_data[offset:end_offset])
                shapeFile.write(new_file_byte_array)
        else:
            print("using extract.exe to extract " + dest_dir + "/" + filename + ", compression type:", info.compression_type)
            subprocess.call(["extract.exe", import_filename, info.filename, dest_dir + "/" + filename])




def extract_archive(import_filename, archive_module):
    with open(import_filename, "rb") as input_fd:
        raw_data = input_fd.read()

    dest_dir = import_filename.replace(".vol", "").replace(".VOL", "")

    file_info = archive_module.get_file_metadata(raw_data)

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    write_files(import_filename, raw_data, dest_dir, file_info)