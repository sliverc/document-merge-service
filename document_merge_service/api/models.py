from django.db import models


class Template(models.Model):
    DOCX_TEMPLATE = "docx-template"
    DOCX_MAILMERGE = "docx-mailmerge"
    ENGINE_CHOICES_LIST = (DOCX_TEMPLATE, DOCX_MAILMERGE)
    ENGINE_CHOICES_TUPLE = (
        (
            DOCX_TEMPLATE,
            "Docx Template engine (https://github.com/elapouya/python-docx-template)",
        ),
        (
            DOCX_MAILMERGE,
            "Docx MailMerge engine (https://github.com/Bouke/docx-mailmerge",
        ),
    )

    name = models.CharField(max_length=255, unique=True)
    template = models.FileField(max_length=1024, upload_to="templates")
    engine = models.CharField(max_length=20, choices=ENGINE_CHOICES_TUPLE)
