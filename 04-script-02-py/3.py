#!/usr/bin/env python3

import sys
import os

if len(sys.argv) < 2:
    print("Path repository not found.")
    exit(1)

dir_repo = sys.argv[1]
path_repo = os.path.abspath(os.path.expanduser(os.path.expandvars(dir_repo)))

if not os.path.isdir('{}/.git'.format(path_repo)):
    print("Repository not found.")
    exit(2)

bash_command = ["cd {}".format(dir_repo), "git status"]
result_os = os.popen(' && '.join(bash_command)).read()

is_change = False
for result in result_os.split('\n'):
    if result.find('modified:') != -1:
        prepare_result = result.replace('\tmodified:', '').strip()
        print('{}/{}'.format(path_repo, prepare_result))
