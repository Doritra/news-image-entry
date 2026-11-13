import os
import shutil

"""
This program copies entry.png from the script directory to the output directory.
"""

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(script_dir, "entry.png")
    
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    
    os.makedirs(out_dir, exist_ok=True)
    
    dest_path = os.path.join(out_dir, "entry.png")
    
    shutil.copyfile(src_path, dest_path)  # Copies entry.png to the output directory

if __name__ == "__main__":
    main()
