from http.client import HTTPResponse
from io import BytesIO
from unittest import result
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse


class GeraPDFMixin:
    def render_to_pdf(self, template_end, context_dict={}):
        template = get_template(template_end)
        html = template.render(context_dict)
        result = BytesIO()
        # try:
        pdf = pisa.pisaDocument(BytesIO(html.encode("utf-8")), result)
        if not pdf.err:
            return HttpResponse(result.getvalue(), content_type='application/pdf')
        return None
        # except Exception as e:
        #     print(e)
        #     return None