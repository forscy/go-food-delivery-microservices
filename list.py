import os

# Tentukan path ke folder 'lib' dalam proyek Flutter
flutter_lib_directory = '.'

# Simpan output ke file
output_file = 'struktur-project.txt'

# Daftar folder dan file yang di-blacklist
blacklisted_folders = {'.dart_tool', '.idea', 'build', '.git', 'android', 'ios', 'web', 'test', 'windows', 'linux', 'macos', 'github'}
blacklisted_files = {'README.md'}

# Normalize blacklisted folder names to match the directory structure
blacklisted_folders = {os.path.normpath(folder) for folder in blacklisted_folders}

with open(output_file, 'w') as f:
    for root, dirs, files in os.walk(flutter_lib_directory):
        # Filter folder yang di-blacklist secara eksplisit dengan membandingkan dengan path penuh
        dirs[:] = [d for d in dirs if os.path.normpath(os.path.join(root, d)) not in blacklisted_folders]
        
        for file in files:
            # Skip file yang di-blacklist
            if file in blacklisted_files:
                continue
            
            file_path = os.path.join(root, file)
            f.write(file_path + '\n')
            print(file_path)
