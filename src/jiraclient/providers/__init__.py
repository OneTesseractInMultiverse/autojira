from jiraclient.abs import AbstractTemplateProvider
import json


class LocalFileVPCNgTemplateProvider(AbstractTemplateProvider):

    def load_template_as_dict(self) -> str:
        with open('vpc_ng_vuln_template.json', 'r') as template_file:
            return template_file.read()
