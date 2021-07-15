from pydantic import BaseModel, Field
from typing import List, Dict, Optional
import datetime


class JiraIssueBase(BaseModel):

    id: Optional[str] = Field(None, title='The Jira issue ID assigned by Jira when the issue gets created')
    project_id: str = Field(None, title='The Jira Project ID where the issue will be created')
    summary: str = Field(None, title='The title of the issue')
    description: str = Field(None, title='The description of the issue')


class VPCNgVulnerabilityJiraIssue(JiraIssueBase):

    due_date: str = Field(None, title='The due date for remediation of the vulnerability')
    team: str = Field(None, title='The name of the team responsible for remediation')
    priority: str = Field(None, title='The priority or severity of the vulnerability')
    issue_type_id: str = Field('3', title='The issue type')
