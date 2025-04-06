import csv


def load_existing_excuses(excuses_csv):
    excuses = set()
    try:
        with open(excuses_csv, newline="", encoding="utf-8") as file:
            reader = csv.reader(file, delimiter=";")
            next(reader, None)  # skip header
            for row in reader:
                excuses.add((row[0], row[1]))
    except FileNotFoundError:
        pass
    return excuses


def save_excuse(excuses_csv, excuse, translated_excuse):
    with open(excuses_csv, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        if file.tell() == 0:
            writer.writerow(["Original", "Traduzida"])  # write header
        writer.writerow([excuse, translated_excuse])
