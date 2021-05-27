'''This script will fetch and count labels for  all issues from Github in the following repos.'''

import requests

# sets 3rd party Nerdpacks repo names

nerdpack_repo_names = ['nr1-github', 'nr1-account-maturity', 'nr1-browser-analyzer', 'nr1-cloud-optimize',  'nr1-container-explorer', 'nr1-datalyzer', 'nr1-deployment-analyzer', 'nr1-event-stream', 'nr1-graphiql-notebook', 'nr1-groundskeeper', 'nr1-integrations-manager',
                       'nr1-learn-nrql', 'nr1-metrics-aggregator', 'nr1-neon', 'nr1-network-telemetry', 'nr1-nimbus', 'nr1-observability-maps', 'nr1-pageview-map', 'nr1-pathpoint', 'nr1-quickstarts', 'nr1-slo-r', 'nr1-status-pages', 'nr1-tag-improver', 'nr1-top', 'nr1-workload-geoops']

# sets Developer ToolKit repos names

dtk_repo_names = ['infrastructure-agent-ansible', 'infrastructure-agent-chef', 'infrastructure-agent-puppet', 'tutone', 'terraform-provider-newrelic',
                  'terraform-newrelic-apm', 'newrelic-cloudformation', 'newrelic-cli', 'newrelic-kubernetes-operator', 'newrelic-client-go', 'developer-toolkit']


def print_issue(issue):
    '''prints issues'''

    labels = ', '.join([label['name'] for label in issue.get('labels', [])])

    print(f"""
Repo: {issue['repository_url']}
ID: {issue['id']}
Title: {issue['title']}
Labels: {labels}
    """)


def repo_fetch():
    '''fetches all issues from repos and returns a count of labels'''

    labels_count = {}

    for repo in dtk_repo_names:
        response = requests.get(
            f'https://api.github.com/repos/newrelic/{repo}/issues'
        )
        if response:
            for issue in response.json():
                print_issue(issue)
                for label in issue.get('labels', []):
                    labels_count[label['name']] = (
                        labels_count.setdefault(label['name'], 0) + 1
                    )
        else:
            print('Error: Not Found.')

    print(labels_count)

if __name__ == '__main__':
    repo_fetch()
