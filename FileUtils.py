import io
from Constants import Constants


class FileUtils:
    def __init__(self):
        pass

    # Functia va scrie datele intr-un fisier txt
    def writeToTxt(self, article_items):
        header = Constants.file_header
        open(Constants.file_name, 'w').close()
        with open(Constants.file_name, 'a') as f:
            f.write(header + "\n")
            f.close

        with io.open(Constants.file_name, "a", encoding="utf-8") as f:
            for article in article_items:
                attrs = vars(article)
                content = (10 * " ").join("%s" % item[1] for item in attrs.items())
                f.write(content + "\n")

            f.close

    # Functia va citi datele din fisier
    def readFromTxt(self, file_name):
        with io.open(file_name, 'r', encoding="utf-8") as f:
            lines = f.readlines()
        col_names = lines[0].strip().split(" ")[1:]
        row_names = []
        data = []
        for line in lines[1:]:
            line_parts = line.strip().split(10 * " ")
            row_names.append(line_parts[0])
            data.append([float(x) for x in line_parts[1:]])
        return row_names, col_names, data