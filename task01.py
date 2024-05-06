import os
import shutil
import sys

def sort_files(src_dir, dst_dir="dist"):
        # Створення директорії призначення, якщо вона не існує
        try:
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
        except OSError as e:
            print(f"Помилка при створенні директорії: {e}")
            return


        # Перебір елементів у вихідній директорії
        for item in os.listdir(src_dir):
            item_path = os.path.join(src_dir, item)

            # Перевірка, чи є елемент директорією
            if os.path.isdir(item_path):
                # Рекурсивний виклик функції для піддиректорії
                try:
                    sort_files(item_path, dst_dir)
                except OSError as e:
                    print(f"Помилка при обробці директорії {item_path}: {e}")
                    continue

            # Перевірка, чи є елемент файлом
            elif os.path.isfile(item_path):
                # Отримання розширення файлу
                try:
                    filename, extension = os.path.splitext(item)

                    # Створення шляху до директорії для типу файлу
                    file_type_dir = os.path.join(dst_dir, extension[1:])

                    # Створення директорії для типу файлу, якщо вона не існує
                    if not os.path.exists(file_type_dir):
                        os.makedirs(file_type_dir)

                    # Копіювання файлу до відповідної директорії
                    shutil.copy2(item_path, file_type_dir)
                except OSError as e:
                    print(f"Помилка при копіюванні файлу {item_path}: {e}")
                    continue
                
# Обробка аргументів командного рядка
if __name__ == "__main__":
    
    if len(sys.argv) < 2:
        print("Необхідно вказати шлях до вихідної директорії.")
        sys.exit(1)

    src_dir = sys.argv[1]

    # Установка шляху до директорії призначення за замовчуванням
    if len(sys.argv) == 2:
        dst_dir = "dist"
    else:
        dst_dir = sys.argv[2]

    # Запуск сортування файлів
    sort_files(src_dir, dst_dir)
