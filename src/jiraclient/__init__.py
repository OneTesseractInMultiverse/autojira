from jiraclient.abs import AbstractTemplateProvider
from jiraclient.models import JiraIssueBase
import jsonplus as json


class IssueMapper(object):

    def __init__(
            self,
            issue: JiraIssueBase,
            template_provider: AbstractTemplateProvider
    ):
        self.template = template_provider.load_template_as_dict()
        self.issue_data = issue.dict()
        self._map()

    def _map(self) -> None:
        for key in self.issue_data.keys():
            if f'%{key}%' in self.template:
                self.template = self.template.replace(
                    f'%{key}%',
                    self.issue_data[key]
                )

    def dict(self):
        return json.loads(self.template)