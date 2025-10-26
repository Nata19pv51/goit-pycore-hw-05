

def parse_log_line(line: str) -> dict:
    words_lst = line.split(" ")
    log_dict = dict()
    log_dict["date"] = words_lst[0]
    log_dict["time"] = words_lst[1]
    log_dict["level"] = words_lst[2]
    separator = " "
    log_dict["message"] = separator.join(words_lst[3:])

    return log_dict

def load_logs(file_path: str) -> list:
    file_lst = []
    
    with open(file_path, "r") as f:
        
        while True:
            line = f.readline()
            if not line:
                break
            
            file_lst.append(parse_log_line(line))
    
    return file_lst
    
def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_list = []
    even_nums = filter(lambda logs: line["level"] for line in logs), range(1, 11))
    # Фільтрацію за рівнем логування 
    # отримати всі записи логу для певного рівня логування
    return filtered_list


list_file = load_logs("log.txt")
print(list_file)



# def count_logs_by_level(logs: list) -> dict:
#     # проходить по всім записам і підраховує кількість записів для кожного рівня логування

# def display_log_counts(counts: dict):
#     # Вивід результатів 
#     # форматує та виводить результати підрахунку в читабельній формі

# види помилок: відсутність файлу, помилки при його читанні, неправильний формат лог-файлу

# При розробці обов'язково було використано один з елементів функціонального програмування: 
# лямбда-функція, списковий вираз, функція filter, тощо