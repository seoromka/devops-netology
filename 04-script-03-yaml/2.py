#!/usr/bin/env python3

import os
import socket
import json
import yaml

domains_file = '2-domains.txt'
domains_result_json_file = './2-domains-result.json'
domains_result_yaml_file = './2-domains-result.yml'


def get_dict_json_file(filename):
    if os.path.isfile(filename):
        try:
            with open(filename) as json_file:
                return json.load(json_file)
        except Exception as err:
            print('Read file error: {}'.format(err))

    return dict()


def set_json_file_dict(filename, data):
    with open(filename, 'w') as fp:
        json.dump(data, fp)


def set_yaml_file_dict(filename, data):
    with open(filename, 'w') as fp:
        yaml.dump(data, fp)


domains = [line.strip() for line in open(domains_file, 'r')]
latest_results = get_dict_json_file(domains_result_json_file)
results = dict()

for domain in domains:
    ip_domain = socket.gethostbyname(domain)
    latest_ip_domain = latest_results.get(domain)
    if latest_ip_domain and latest_ip_domain != ip_domain:
        print('[ERROR] {} IP mismatch: {} {}.'.format(domain, latest_ip_domain, ip_domain))
    else:
        print('{} - {}'.format(domain, ip_domain))
    results[domain] = ip_domain

set_json_file_dict(domains_result_json_file, results)
set_yaml_file_dict(domains_result_yaml_file, results)
