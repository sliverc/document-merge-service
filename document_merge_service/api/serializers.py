import zipfile

from docx import Document
from rest_framework import exceptions, serializers

from . import models


class TemplateSerializer(serializers.ModelSerializer):
    # TODO: add README.md how to use it
    # TODO: integrate unoconv service
    # TODO: add command to clean ununsed templates

    def validate(self, data):
        template = data["template"]

        # TODO: engine should also expose validation
        try:
            Document(template)
        except (ValueError, zipfile.BadZipfile):
            raise exceptions.ParseError("not a valid docx file")

        template.seek(0)
        return template

    class Meta:
        model = models.Template
        fields = ("name", "template", "engine")


class TemplateMergeSerializer(serializers.Serializer):
    data = serializers.JSONField(required=True)
