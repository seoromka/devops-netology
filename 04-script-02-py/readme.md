### Как сдавать задания

Вы уже изучили блок «Системы уп### Как сдавать задания

Вы уже изучили блок «Системы управления версиями», и начиная с этого занятия все ваши работы будут приниматься ссылками на .md-файлы, размещённые в вашем публичном репозитории.

Скопируйте в свой .md-файл содержимое этого файла; исходники можно посмотреть [здесь](https://raw.githubusercontent.com/netology-code/sysadm-homeworks/devsys10/04-script-02-py/README.md). Заполните недостающие части документа решением задач (заменяйте `???`, ОСТАЛЬНОЕ В ШАБЛОНЕ НЕ ТРОГАЙТЕ чтобы не сломать форматирование текста, подсветку синтаксиса и прочее, иначе можно отправиться на доработку) и отправляйте на проверку. Вместо логов можно вставить скриншоты по желани.

# Домашнее задание к занятию "4.2. Использование Python для решения типовых DevOps задач"

## Обязательная задача 1

Есть скрипт:
```python
#!/usr/bin/env python3
a = 1
b = '2'
c = a + b
```

### Вопросы:
| Вопрос  | Ответ |
| ------------- | ------------- |
| Какое значение будет присвоено переменной `c`?  | будет ошибка типов. Строки и числа нельзя складывать  |
| Как получить для переменной `c` значение 12?  | `c = str(a) + b`  |
| Как получить для переменной `c` значение 3?  | `c = a + int(b)`  |

## Обязательная задача 2
Мы устроились на работу в компанию, где раньше уже был DevOps Engineer. Он написал скрипт, позволяющий узнать, какие файлы модифицированы в репозитории, относительно локальных изменений. Этим скриптом недовольно начальство, потому что в его выводе есть не все изменённые файлы, а также непонятен полный путь к директории, где они находятся. Как можно доработать скрипт ниже, чтобы он исполнял требования вашего руководителя?

```python
#!/usr/bin/env python3

import os

bash_command = ["cd ~/netology/sysadm-homeworks", "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(prepare_result)
        break
```

### Ваш скрипт:
```python
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
```

### Вывод скрипта при запуске при тестировании:
```
/Users/rk/sysadm-homeworks/02-git-01-vcs/README.md
/Users/rk/sysadm-homeworks/README.md
```

## Обязательная задача 3
1. Доработать скрипт выше так, чтобы он мог проверять не только локальный репозиторий в текущей директории, а также умел воспринимать путь к репозиторию, который мы передаём как входной параметр. Мы точно знаем, что начальство коварное и будет проверять работу этого скрипта в директориях, которые не являются локальными репозиториями.

### Ваш скрипт:
```python
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
```

### Вывод скрипта при запуске при тестировании:
```
rk@MacBook-Pro-Roman-2 04-script-02-py % python3 3.py ~/sysadm-homeworks11
    Repository not found.
    
rk@MacBook-Pro-Roman-2 04-script-02-py % python3 3.py ~/sysadm-homeworks
    /Users/rk/sysadm-homeworks/02-git-01-vcs/README.md
    /Users/rk/sysadm-homeworks/README.md
```

## Обязательная задача 4
1. Наша команда разрабатывает несколько веб-сервисов, доступных по http. Мы точно знаем, что на их стенде нет никакой балансировки, кластеризации, за DNS прячется конкретный IP сервера, где установлен сервис. Проблема в том, что отдел, занимающийся нашей инфраструктурой очень часто меняет нам сервера, поэтому IP меняются примерно раз в неделю, при этом сервисы сохраняют за собой DNS имена. Это бы совсем никого не беспокоило, если бы несколько раз сервера не уезжали в такой сегмент сети нашей компании, который недоступен для разработчиков. Мы хотим написать скрипт, который опрашивает веб-сервисы, получает их IP, выводит информацию в стандартный вывод в виде: <URL сервиса> - <его IP>. Также, должна быть реализована возможность проверки текущего IP сервиса c его IP из предыдущей проверки. Если проверка будет провалена - оповестить об этом в стандартный вывод сообщением: [ERROR] <URL сервиса> IP mismatch: <старый IP> <Новый IP>. Будем считать, что наша разработка реализовала сервисы: `drive.google.com`, `mail.google.com`, `google.com`.

### Ваш скрипт:
```python
#!/usr/bin/env python3

import os
import socket
import json

domains_file = './4-domains.txt'
domains_result_file = './4-domains-result.json'


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


domains = [line.strip() for line in open(domains_file, 'r')]
latest_results = get_dict_json_file(domains_result_file)
results = dict()

for domain in domains:
    ip_domain = socket.gethostbyname(domain)
    latest_ip_domain = latest_results.get(domain)
    if latest_ip_domain and latest_ip_domain != ip_domain:
        print('[ERROR] {} IP mismatch: {} {}.'.format(domain, latest_ip_domain, ip_domain))
    else:
        print('{} - {}'.format(domain, ip_domain))
    results[domain] = ip_domain

set_json_file_dict(domains_result_file, results)
```

### Вывод скрипта при запуске при тестировании:
```
rk@MacBook-Pro-Roman-2 04-script-02-py % python 4.py
    drive.google.com - 173.194.205.139
    mail.google.com - 172.217.17.101
    google.com - 142.250.187.142

rk@MacBook-Pro-Roman-2 04-script-02-py % python 4.py
    [ERROR] drive.google.com IP mismatch: 173.194.205.13 173.194.205.139.
    mail.google.com - 172.217.17.101
    google.com - 142.250.187.142
```
