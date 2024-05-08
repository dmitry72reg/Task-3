import os


def merge_files(files):
    file_info = []
    for i, file in enumerate(files):
        with open(file, 'r') as f:
            lines = f.readlines()
            line_count = len(lines)
            file_info.append((line_count, i, file, lines))
    file_info.sort()
    merged_file = open('merged_file.txt', 'w')
    for line_count, i, file, lines in file_info:
        merged_file.write(f"{os.path.basename(file)}\n{line_count}\n")
        for j, line in enumerate(lines):
            merged_file.write(f"Строка номер {j + 1} файла номер {i + 1}\n")
        merged_file.write("")
    merged_file.close()
    print(open('merged_file.txt', 'r').read())


merge_files(['1.txt', '2.txt'])
