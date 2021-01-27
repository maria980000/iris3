import json
from test_scripts.utils_for_tests import do_local_http

"""
This integration test is useful in development. Run main.py in debug mode, then run 
test_do_label.

Comment or uncomment resource types in `test_do_label` to focus the testing.
"""


def test_do_label():
    project = "joshua-playground-host-vpc"
    plugins = [
        # 'Buckets', 'Bigquery',
        "Instances",
        # 'Disks', 'Snapshots',
        # 'Topics',
        # "Subscriptions",
        # 'Cloudsql',
        # 'Bigtable'
    ]

    for plugin in plugins:
        contents = json.dumps({"project_id": project, "plugin": plugin})
        do_local_http("do_label", contents)


if __name__ == "__main__":
    test_do_label()
