##
## Scans your hard drive to find the 200 largest files
##

import os

def get_folder_tree( parent_folder, recursive=True ):
    files = []
    if recursive:
        for root, dirlist, filelist in os.walk(parent_folder):
            for name in filelist:
                full_name = os.path.join(root, name)
                try:
                    mtime = os.path.getmtime( full_name )
                    size = os.path.getsize( full_name )
                    absolute = os.path.abspath( full_name )
                    last_seperator = absolute.rindex( os.sep )
                    parent_folder = absolute[ : last_seperator ]
                    local_file_name = absolute[ last_seperator+1 : ]
                    extension = ""
                    if "." in local_file_name:
                        extension_location = local_file_name.rindex(".")
                        extension = local_file_name[ extension_location+1 : ]
                    result = { 
                        "type":         "file", 
                        "parent":       parent_folder, 
                        "name":         local_file_name, 
                        "extension":    extension,
                        "absolute":     absolute,
                        "mtime":        mtime, 
                        "size":         size
                    }
                    files.append( result )
                except:
                    print(f"[error] failed to read: {full_name}")
            for name in dirlist:
                full_name = os.path.join(root, name)
                relative_folder = root[ len(parent_folder): ]
                rec = { 
                    "type":     "folder", 
                    "parent":   relative_folder, 
                    "name":     name,
                    "absolute": full_name,
                    "size": 0
                }
                files.append(rec)
    return(files)

if __name__ == "__main__":
    print(f"Searching your system for all files & folders...")
    inf = get_folder_tree("C:/", recursive=True)
    print(f"Found {len(inf)} items.")
    print(f"Sorting...")
    inf = sorted(inf, key=lambda s: s['size'], reverse=True)
    display_count = min([len(inf), 200])
    for i in range(display_count):
        print_size = int(inf[i]['size']) // (2**20) # megabytes
        print(f"{print_size:5}Mb = {inf[i]['absolute']}")
