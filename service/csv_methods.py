import csv
from service.models.db_add_method import add_data_in_db
from service.serializers import Waterfall

csv_file = "C:\\project\\whereze\\backend\\waterfalls_details.csv"


def read_and_wite_csv(filename):
    all_waterfalls = []
    with open(filename, 'w', encoding='utf-8') as f:
        fields = ['title', 'summary', 'url',
                  'height', 'width', 'river',
                  'country', 'region', 'subject_RF']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for row in all_waterfalls:
            writer.writerow(row)

    with open(filename, "r", encoding="utf-8") as f:
        fields = ['title', 'summary', 'url',
                  'height', 'width', 'river',
                  'country', 'region', 'RF_subject']
        reader = csv.DictReader(f, fields, delimiter=';')
        next(reader)


def add_csv_in_db(filename):
    with open(filename, "r", encoding="utf-8") as f:
        fields = ['title', 'summary', 'url',
                  'height', 'width', 'river',
                  'country', 'region', 'RF_subject']
        reader = csv.DictReader(f, fields, delimiter=';')
        next(reader)
        uid_number = 1
        for row in reader:
            row['uid'] = uid_number
            letter = filter(str.isdecimal, row['height'])
            row['height'] = "".join(letter)
            letter = filter(str.isdecimal, row['width'])
            row['width'] = "".join(letter)
            uid_number += 1
            Waterfall(**row)
            add_data_in_db(row)


if __name__ == "__main__":
    add_csv_in_db(csv_file)
