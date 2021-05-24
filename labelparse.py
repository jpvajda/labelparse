'''This script will fetch and all issues from Github in the following repos.'''

import requests


# sets 3rd party Nerdpacks repo names

nerdpack_repo_names = ['nr1-github', 'nr1-account-maturity', 'nr1-browser-analyzer', 'nr1-cloud-optimize',  'nr1-container-explorer', 'nr1-datalyzer', 'nr1-deployment-analyzer', 'nr1-event-stream', 'nr1-graphiql-notebook', 'nr1-groundskeeper', 'nr1-integrations-manager',
                       'nr1-learn-nrql', 'nr1-metrics-aggregator', 'nr1-neon', 'nr1-network-telemetry', 'nr1-nimbus', 'nr1-observability-maps', 'nr1-pageview-map', 'nr1-pathpoint', 'nr1-quickstarts', 'nr1-slo-r', 'nr1-status-pages', 'nr1-tag-improver', 'nr1-top', 'nr1-workload-geoops']

# sets Developer ToolKit repos names

dtk_repo_names = ['infrastructure-agent-ansible', 'infrastructure-agent-chef', 'infrastructure-agent-puppet', 'tutone', 'terraform-provider-newrelic',
                  'terraform-newrelic-apm', 'newrelic-cloudformation', 'newrelic-cli', 'newrelic-kubernetes-operator', 'newrelic-client-go', 'developer-toolkit']


def print_labels(issue):
    '''Loops through repo data'''

    if 'labels' in issue and issue['labels'] != []:
        for label in issue['labels']:
            print('Label: ' + label['name'])


def print_issue(issue):
    '''prints issues'''

    if response.status_code == 200:
        print('\n')
        print('Repo: ' + issue['repository_url'])
        print('ID: ' + str(issue['id']))
        print('Title: ' + issue['title'])
        print_labels(issue)
    else:
        print('Error: Not Found.')

# Fetches repo data


for repo in dtk_repo_names:
    response = requests.get(
        'https://api.github.com/repos/newrelic/' + str(repo) + '/issues')

    for issue in response.json():
        print_issue(issue)


# @todo return a count of each label type.
# for each issue
#   for each label
#     if we have a count for this label, +1
#     if we don't have a count for this label, make one and set to 1
