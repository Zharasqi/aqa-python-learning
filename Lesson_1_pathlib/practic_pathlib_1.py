from pathlib import Path

folder = Path("test_data")
folder_path = folder.rglob("*.txt")

for txt_files in folder_path:
    print(txt_files)



# folder = Path("test_data") / "practice"
# file_name = folder / "hello.txt"
# file_name.write_text("Первая строка добавлена", encoding="utf-8")
# print(file_name.exists())
# print(file_name.read_text())


# folder_name = Path("test_data") / "practice"
# folder_name.mkdir(exist_ok=True)
# print(folder_name.exists())



# full_path = Path("test_data") / "user.txt"
# file_name = Path("test_data")
#
# print(full_path.exists())
# print(file_name.exists())




# file_path = Path("json_learning_summary.md")
# print(file_path.exists())
# print(file_path.name)
# print(file_path.suffix)
# print(file_path.parent)