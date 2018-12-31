import io

from docxtpl import DocxTemplate
from mailmerge import MailMerge


class DocxTemplateEngine:
    def __init__(self, template):
        self.template = template

    def merge(self, data):
        doc = DocxTemplate(self.template)
        doc.render(data)
        buf = io.BytesIO()
        doc.save(buf)
        buf.seek(0)

        return buf


class DocxMailmergeEngine:
    def __init__(self, template):
        self.template = template

    def merge(self, data):
        with MailMerge(self.template) as document:
            document.merge(**data)
            buf = io.BytesIO()
            document.write(buf)
            buf.seek(0)
            return buf
