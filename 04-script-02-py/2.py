#!/usr/bin/env python3

import os

bash_command = ["cd ~/sysadm-homeworks", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()

path_repo_abspath = bash_command[0].split()[1]
path_repo = os.path.abspath(os.path.expanduser(os.path.expandvars(path_repo_abspath)))

is_change = False
for result in result_os.split('\n'):
    if result.find('modified:') != -1:
        prepare_result = result.replace('\tmodified:', '').strip()
        print('{}/{}'.format(path_repo, prepare_result))
