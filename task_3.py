from collections import Counter
import sys


def parse_log_line(line: str) -> dict:
    words_lst = line.split(" ")
    # Parse the line and form a dictionary:
    log_dict = dict()
    log_dict["date"] = words_lst[0]
    log_dict["time"] = words_lst[1]
    log_dict["level"] = words_lst[2]
    separator = " "
    log_dict["message"] = separator.join(words_lst[3:])

    return log_dict

def load_logs(file_path: str) -> list:
    file_lst = []
    try:
        # Read the file and parse lines. Get list of dictionaries:
        with open(file_path, "r") as f:
            
            while True:
                line = f.readline()
                if not line:
                    break
                file_lst.append(parse_log_line(line))
    
    except FileNotFoundError:
        # Handle the case where the file is not found
        print("Error: The specified file was not found.")  
    
    else:
        return file_lst
    
def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_list = filter(lambda item: item['level'] == level, logs)
    filtered_list = list(filtered_list)
    return filtered_list

def count_logs_by_level(logs: list) -> dict:
    levels_list = []
    
    # Fill the empty list with levels
    for item in logs:
        levels_list.append(item["level"])

    return Counter(levels_list)

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    for key, value in counts.items():
        print(f"{key:<17}| {value:<9}")


if __name__ == "__main__":
    file = sys.argv[1]
    list_file = load_logs(file)
    levels_count = count_logs_by_level(list_file)

    if len(sys.argv) > 2:
        first_argument = sys.argv[2].upper()
        
        # Print error levels and their counts:
        display_log_counts(levels_count)
        
        print(f"\nДеталі логів для рівня \'{first_argument}\':")
        
        # Filter logs by level entered from consol:
        filtered_lst = filter_logs_by_level(list_file, first_argument)

        # Print the filtered logs by level:
        for item in filtered_lst:
            print(" ".join(list(item.values())).rstrip("\n"))
    else:
        # If the user doesn't enter error level, print ingo about all levels and their counts:
        display_log_counts(levels_count)