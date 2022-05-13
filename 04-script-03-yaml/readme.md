## Обязательная задача 1
Мы выгрузили JSON, который получили через API запрос к нашему сервису:
```
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            }
            { "name" : "second",
            "type" : "proxy",
            "ip : 71.78.22.43
            }
        ]
    }
```
  Нужно найти и исправить все ошибки, которые допускает наш сервис

```
    { "info" : "Sample JSON output from our service\t",
        "elements" :[
            { "name" : "first",
            "type" : "server",
            "ip" : 7175 
            }, // не хватает запятой между объектами
            { "name" : "second",
            "type" : "proxy",
            "ip : "71.78.22.43" // значение должно быть строкой
            }
        ]
    }
```

## Обязательная задача 2
В прошлый рабочий день мы создавали скрипт, позволяющий опрашивать веб-сервисы и получать их IP. К уже реализованному функционалу нам нужно добавить возможность записи JSON и YAML файлов, описывающих наши сервисы. Формат записи JSON по одному сервису: `{ "имя сервиса" : "его IP"}`. Формат записи YAML по одному сервису: `- имя сервиса: его IP`. Если в момент исполнения скрипта меняется IP у сервиса - он должен так же поменяться в yml и json файле.

### Ваш скрипт:
```python
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
```

### Вывод скрипта при запуске при тестировании:
```
python3 ./2.py
```

### json-файл(ы), который(е) записал ваш скрипт:
```json
{"drive.google.com": "173.194.205.139", "mail.google.com": "172.217.169.133", "google.com": "172.217.17.142"}
```

### yml-файл(ы), который(е) записал ваш скрипт:
```yaml
drive.google.com: 173.194.205.139
google.com: 172.217.17.142
mail.google.com: 172.217.169.133
```
