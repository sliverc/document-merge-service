import mimetypes

from django.http import HttpResponse
from django.utils.encoding import smart_str
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView

from . import engines, models, serializers


class TemplateView(viewsets.ModelViewSet):
    queryset = models.Template.objects
    serializer_class = serializers.TemplateSerializer
    filterset_fields = {"name": ["exact", "iexact", "contains", "icontains"]}
    ordering_fields = ("name",)
    ordering = ("name",)
    engines = {
        models.Template.DOCX_TEMPLATE: engines.DocxTemplateEngine,
        models.Template.DOCX_MAILMERGE: engines.DocxMailmergeEngine,
    }

    def get_engine(self, template):
        return self.engines[template.engine](template.template)

    @action(
        methods=["post"],
        detail=True,
        serializer_class=serializers.TemplateMergeSerializer,
    )
    def merge(self, request, pk=None):
        template = self.get_object()

        response = HttpResponse()
        # TODO: think about file name
        filename = "{0}.{1}".format(template.name, "docx")
        response["Content-Disposition"] = 'attachment; filename="{0}"'.format(filename)
        response["Content-Type"] = mimetypes.guess_type(filename)[0]

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        engine = self.get_engine(template)
        buf = engine.merge(serializer.data["data"])
        response.write(buf.read())

        return response


class DownloadTemplateView(RetrieveAPIView):
    queryset = models.Template.objects
    # TODO: consider easier readable url
    lookup_field = "template"

    def retrieve(self, request, **kwargs):
        template = self.get_object()

        mime_type, _ = mimetypes.guess_type(template.template.name)
        extension = mimetypes.guess_extension(mime_type)
        content_type = mime_type or "application/force-download"

        response = HttpResponse(content_type=content_type)
        response["Content-Disposition"] = 'attachment; filename="%s"' % smart_str(
            template.name + extension
        )
        response["Content-Length"] = template.template.size
        response.write(template.template.read())
        return response
