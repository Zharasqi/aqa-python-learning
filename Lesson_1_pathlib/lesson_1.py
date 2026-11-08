# from pathlib import Path
#
# current_file = Path(__file__)
# project_root = current_file.parent
# data_file = project_root / "user.json"
#
# print(data_file)
# print(data_file.exists())

from pathlib import Path

folder = Path("reports")
folder.mkdir(exist_ok=True)

file_path = folder / "result.txt"
file_path.write_text("Test passed")

content = file_path.read_text()
print(content)