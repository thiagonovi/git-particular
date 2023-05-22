import ctypes
import shutil
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def copy_file(source_path, destination_path):
    try:
        shutil.copy(source_path, destination_path)
        print("File copied successfully!")
    except FileNotFoundError:
        print("Source file not found.")
    except PermissionError:
        print("Permission denied.")
    except shutil.SameFileError:
        print("Source and destination are the same.")
    except:
        print("An error occurred while copying the file.")

if is_admin():
    # The script is already running with administrative privileges
    # Example usage
    source_file = r'C:\path\to\source\file.txt'
    destination_folder = r'C:\path\to\destination\folder'

    copy_file(source_file, destination_folder)
else:
    # Re-run the script with administrative privileges
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
