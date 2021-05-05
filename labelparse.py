import json
import requests


# sets reponames

reponames = ['nr1-github', 'nr1-account-maturity', 'nr1-browser-analyzer', 'nr1-cloud-optimize',  'nr1-container-explorer', 'nr1-datalyzer', 'nr1-deployment-analyzer', 'nr1-event-stream', 'nr1-graphiql-notebook', 'nr1-groundskeeper', 'nr1-integrations-manager',
             'nr1-learn-nrql', 'nr1-metrics-aggregator', 'nr1-neon', 'nr1-network-telemetry', 'nr1-nimbus', 'nr1-observability-maps', 'nr1-pageview-map', 'nr1-pathpoint', 'nr1-quickstarts', 'nr1-slo-r', 'nr1-status-pages', 'nr1-tag-improver', 'nr1-top', 'nr1-workload-geoops']

# Loops through repo data


def print_labels(issue):
    if 'labels' in issue and issue['labels'] != []:
        for label in issue['labels']:
            print('Label: ' + label['name'])


def print_issue(issue):
    print('\n')
    print('Repo: ' + issue['repository_url'])
    print('ID: ' + str(issue['id']))
    print('Title: ' + issue['title'])
    print_labels(issue)

# Fetches repo data


for repo in reponames:
    response = requests.get(
        'https://api.github.com/repos/newrelic/' + str(repo) + '/issues')

    for issue in response.json():
        print_issue(issue)


# @todo add logic for status codes error handling

#  if response.status_code == 200:
#         elif response.status_code == 404:
#         print('Not Found.')


# @todo return a count of each label type.
# for each issue
#   for each label
#     if we have a count for this label, +1
#     if we don't have a count for this label, make one and set to 1
