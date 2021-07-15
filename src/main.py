from jiraclient.abs import AbstractTemplateProvider
from jiraclient.providers import LocalFileVPCNgTemplateProvider
from jiraclient.models import VPCNgVulnerabilityJiraIssue
from jiraclient.models import JiraIssueBase
from jiraclient import IssueMapper
import os
import pprint


if __name__ == '__main__':
    print(os.getcwd())
    template_provider: AbstractTemplateProvider = LocalFileVPCNgTemplateProvider()
    issue: JiraIssueBase = VPCNgVulnerabilityJiraIssue(
        project_id='PR001',
        summary='Test Issue',
        description='This is a test description',
        due_date='10/10/2021',
        team='Example_Team',
        priority='High'
    )

    issue_for_jira = IssueMapper(
        template_provider=template_provider,
        issue=issue
    ).dict()

    pprint.pp(issue_for_jira)




