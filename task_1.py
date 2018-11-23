import re
import csv


files = ["info_1.txt", "info_2.txt", "info_3.txt"]
keys = ["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]
target_csv = "info.csv"

def get_data(files):
    main_data = [keys]
    temp_data = {}
    for file in files:
        with open(file, "r", encoding="cp1251") as fl:
            for row in fl:
                for key in keys:
                    str = re.search(f"(?<={key}:).*$", row)
                    if(str):
                        if(file in temp_data):
                            temp_data[file].append(re.sub("\s[\s+]", "", str.group(0)))
                        else:
                            temp_data[file] = []
                            temp_data[file].append(re.sub("\s[\s+]", "", str.group(0)))
                    else:
                        continue
    for item in files:
        main_data.append(temp_data[item])
    print(main_data)
    return main_data

def write_to_csv():
    with open(target_csv, "w") as csv_file:
        csv_file_writer = csv.writer(csv_file)
        data = get_data(files)
        for row in data:
            csv_file_writer.writerow(row)

write_to_csv()




