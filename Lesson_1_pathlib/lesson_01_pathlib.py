from pathlib import Path

folder_test_data = Path("test_data")
folder_test_data.mkdir(exist_ok=True)

file_path = folder_test_data / 'user.txt'
file_path.write_text(
    "Uzbekbayev Zharas\n"
    "26\n"
    "Almata", encoding="utf-8"
)

user_read = file_path.read_text(encoding="utf-8")
suffix_user = file_path.suffix
is_file = file_path.is_file()

print(f"Файл содержит такие данные: \n{user_read}")
print(folder_test_data.exists())
print(file_path.exists())

if is_file:
    print(f"Файл существует: {is_file}")
else:
    print("Файл не найден или не существует")
print(f"Расширение файла: {suffix_user}")

folder_report = Path("reports")
folder_report.mkdir(exist_ok=True)
summary_file = folder_report / 'summary.txt'
summary_file.write_text(
    "Pathlib homework completed", encoding="utf-8"
)
summary_read = summary_file.read_text(encoding="utf-8")
print()
print(summary_read)