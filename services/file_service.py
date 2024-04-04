import csv


class FileService:
    def write_content(file_name, header, content):
        with open(file_name, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header)
            writer.writerows(content)
