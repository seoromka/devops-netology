# Домашнее задание к занятию "5.2. Применение принципов IaaC в работе с виртуальными машинами"

---

## Задача 1

- Опишите своими словами основные преимущества применения на практике IaaC паттернов.

    ```
  Описываем инфраструктуры в виде простого кода, а чаще всего конфига. 
  Что позволяет нам ускорить разработку и тестирование. 
  Так же мы можем расчитывать, что конфигурация на всех машинах будет одинаковая.
  ```

- Какой из принципов IaaC является основополагающим?

    ```
  Идемпотентность. При каждом развертывании с один и тем же конфигом, мы получим один и тот же результат.
  ```

## Задача 2

- Чем Ansible выгодно отличается от других систем управление конфигурациями?
  
    ```
  Достаточно ssh, не нужен клиент
  ```      


- Какой, на ваш взгляд, метод работы систем конфигурации более надёжный push или pull?

    ```
  push, потому что конфигурацию отправляет управляющий сервер, а не целевые хосты. 
  ```

## Задача 3

Установить на личный компьютер:

- VirtualBox
```
на m1 запускал через parallels, но пробный месяц истек (
Задание 4 пытался сделать docker in docker c использованием vagrant, но возникли трудности с подключением ansible в докер контейнер
```
- Vagrant
```
rk@MacBook-Pro-Roman-2 ~ % vagrant --version
Vagrant 2.2.19
```
- Ansible
```
rk@MacBook-Pro-Roman-2 ~ % ansible --version
ansible [core 2.12.4]
  config file = None
  configured module search path = ['/Users/rk/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /opt/homebrew/Cellar/ansible/5.6.0/libexec/lib/python3.10/site-packages/ansible
  ansible collection location = /Users/rk/.ansible/collections:/usr/share/ansible/collections
  executable location = /opt/homebrew/bin/ansible
  python version = 3.10.2 (main, Feb  2 2022, 05:51:25) [Clang 13.0.0 (clang-1300.0.29.3)]
  jinja version = 3.1.1
  libyaml = True
  ```

*Приложить вывод команд установленных версий каждой из программ, оформленный в markdown.*

## Задача 4 (*)

Воспроизвести практическую часть лекции самостоятельно.

- Создать виртуальную машину.
- Зайти внутрь ВМ, убедиться, что Docker установлен с помощью команды
```
docker ps
```