class Document:
    def create(self):
        raise NotImplementedError("Metóda create() musí byť prepísaná.")


class PDFDocument(Document):
    def create(self):
        return "Vytváram PDF dokument."


class WordDocument(Document):
    def create(self):
        return "Vytváram Word dokument."


class ExcelDocument(Document):
    def create(self):
        return "Vytváram Excel dokument."


class TextDocument(Document):
    def create(self):
        return "Vytváram Text dokument."


class Factory:
    def create_document(self, extension):
        if extension == 'pdf':
            return PDFDocument()
        elif extension == 'doc' or extension == 'docx':
            return WordDocument()
        elif extension == 'xls' or extension == 'xlsx':
            return ExcelDocument()
        else:
            raise ValueError("Neznámy typ dokumentu")


factory = Factory()

pdf = factory.create_document('pdf')
print(pdf.create())

word = factory.create_document('doc')
print(word.create())

excel = factory.create_document('xls')
print(excel.create())

# verzia2
class Document:
    def create(self):
        raise NotImplementedError("Metóda create() musí byť prepísaná.")


class PDFDocument(Document):
    def create(self):
        return "Vytváram PDF dokument."


class WordDocument(Document):
    def create(self):
        return "Vytváram Word dokument."


class ExcelDocument(Document):
    def create(self):
        return "Vytváram Excel dokument."


class TextDocument(Document):
    def create(self):
        return "Vytváram Text dokument."


class Factory:
    def create_document(self, extension):
        extension = extension.lower()

        if extension == "pdf":
            return PDFDocument()
        elif extension in ("doc", "docx"):
            return WordDocument()
        elif extension in ("xls", "xlsx"):
            return ExcelDocument()
        elif extension == "txt":
            return TextDocument()
        else:
            raise ValueError(f"Neznámy typ dokumentu: {extension}")


# Použitie
factory = Factory()

for ext in ["pdf", "doc", "xls", "txt"]:
    document = factory.create_document(ext)
    print(document.create())