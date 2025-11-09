import json
import os


class Reader:
    def __init__(self, /, folder_path="", search_deep=False):
        self.folder_path = folder_path
        self.search_deep = search_deep
        self.files = []
        self.selected_files = None

    def read_folder(self, _dir=None):
        folder = _dir or self.folder_path
        if folder == self.folder_path:
            self.files.clear()
        for file_name in os.listdir(folder):
            full_path = os.path.join(folder, file_name)
            if os.path.isfile(full_path):
                self.files.append(file_name)
            elif self.search_deep:
                self.read_folder(full_path)

    def select_file(self):
        self.show_files()
        selected_files = input("Выберите файл! >>\n")
        if selected_files:
            try:
                number = int(selected_files) - 1
                if 0 <= number < len(self.files):
                    self.selected_files = self.files[number]
                else:
                    print("Не удалось выбрать файл")
            except ValueError:
                print("Не удалось выбрать файл")
        else:
            print("Не удалось выбрать файл")

    def show_files(self):
        for i, item in enumerate(self.files, start=1):
            print(f"{i}) {item}")

    def run(self):
        if not self.folder_path:
            self.folder_path = input("Введите путь до папки! >>\n")
        if not self.folder_path or not (os.path.exists(self.folder_path) and os.path.isdir(self.folder_path)):
            self.folder_path = ""
            print("Не удалось прочитать папку")
            return None
        self.read_folder()
        self.select_file()
        return self.selected_files

    def read(self, path=None):
        try:
            _path = path or os.path.join(self.folder_path, self.selected_files)
            with open(_path, 'r', encoding="utf-8") as file:
                return file.read()
        except Exception as e:
            print(f"Произошла ошибка при чтении файла: {e}")
            return None

    def read_json(self):
        try:
            return json.loads(self.read())
        except Exception as e:
            print(f"Ошибка при чтении json: {e}")
            return None

    def write_json(self, data):
        try:
            path = os.path.join(self.folder_path, self.selected_files)
            with open(path, 'w', encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Ошибка при записи: {e}")


def exemple():
    tusks = Reader(search_deep=True)
    data = None
    while data is None:
        data = tusks.run()
    content = tusks.read_json()
    if not content:
        content = []
    content.append(("omar", 1))
    print(content)
    tusks.write_json(content)


if __name__ == "__main__":
    exemple()

