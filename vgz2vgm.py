#PROGRAM WAS MADE BY MR. SATURN (AKA Г-Н САТУРН)
import os
import shutil
import gzip
import shutil

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def extract_and_rename(vgz_path, extract_to):
    try:
        print(f"Попытка открыть файл: {vgz_path}")
        with gzip.open(vgz_path, 'rb') as f_in:
            extracted_file_path = os.path.join(extract_to, os.path.basename(vgz_path)[:-4])  # Убираем .vgz
            with open(extracted_file_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
            print(f"Файл успешно извлечен: {extracted_file_path}")

        if not extracted_file_path.endswith('.vgm'):
            new_file_path = extracted_file_path + '.vgm'
            os.rename(extracted_file_path, new_file_path)
            print(f"Переименован файл: {extracted_file_path} -> {new_file_path}")

    except Exception as e:
        print(f"Ошибка при обработке {vgz_path}: {e}")

def choose_your_path():
    clear()
    print("RU: Выберете путь к папке с файлами .vgz")
    print("EN: Choose your path to the .vgz folder")
    folder_path = input("> ")

    if folder_path == "":
        clear()
        print("RU: Введите путь!")
        print("EN: Enter path!")
        input("> ")
        choose_your_path()
        return

    elif not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        clear()
        print("RU: Некорректный или несуществующий путь!")
        print("EN: Incorrect or non-existent path!")
        input("> ")
        choose_your_path()
        return

    new_folder = os.path.join(folder_path, 'VGM')
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)

    for filename in os.listdir(folder_path):
        if filename.endswith('.vgz'):
            old_file = os.path.join(folder_path, filename)
            print(f"Обрабатываем файл: {old_file}")
            extract_and_rename(old_file, new_folder)

    clear()
    print("RU: Успешно обработаны все файлы!")
    print("EN: Successfully processed all files!")
    input("OK")


choose_your_path()
