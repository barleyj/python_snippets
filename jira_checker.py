from getpass import *
from jira import *
import warnings
import inspect

development = True

message_format = '{}:{} JiraClosed: {} was closed on {}. Consider fixing this code.'
user = None
password = None
jira = None


def get_credentials():
    global jira
    global user
    global password
    if jira is None:
        user = getuser()
        password = getpass()
        jira = JIRA('https://jira.com', basic_auth=(user, password))
        print ''

checked = set()


def jira_issues(*ids):
    ids_to_check = set(ids)
    ids_to_check -= checked

    if development and ids:
        get_credentials()

        for id in ids_to_check:
            issue = jira.issue(id)
            if issue.fields.status.name == 'Closed':
                filename, line_number = inspect.getouterframes(
                    inspect.currentframe())[1][1:3]

                warning = message_format.format(filename, line_number, id,
                                                str(issue.fields.resolutiondate))
                print(warning)
                checked.add(id)

    def check_jira(fun):
        return fun
    return check_jira


@jira_issues('RSNT-1192', 'RSNT-1191')
def test():
    print 'OMG this is my terrible work around'

test()
