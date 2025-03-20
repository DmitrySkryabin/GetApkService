import os
from datetime import datetime

def get_sorted_files_by_date(directory):
    # Получаем список файлов в указанной директории
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    
    # Создаем список кортежей (файл, дата изменения)
    files_with_dates = []
    for file in files:
        file_path = os.path.join(directory, file)
        # Получаем время последнего изменения файла
        modification_time = os.path.getmtime(file_path)
        # Преобразуем время в читаемый формат
        modification_date = datetime.fromtimestamp(modification_time)
        files_with_dates.append((file, modification_date))
    
    # Сортируем файлы по дате изменения
    sorted_files = sorted(files_with_dates, key=lambda x: x[1])
    
    return sorted_files