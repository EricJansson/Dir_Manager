from pathlib import Path

directory_path = Path('/path/to/your/folder')
directory_path = Path('folder') / 'subfolder' / 'file.txt'
contents = directory_path.iterdir()
for item in contents:
    print(item.name)
