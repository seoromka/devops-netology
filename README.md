# devops netology course

В папке terraform будут проигнорированы:
- все файлы расположенные в папках с названием `.terraform` 
- все файлы с расширениями `.tfstate`, `.tfvars`
- все файлы в имени которых содержиться `.tfstate.`
- все файлы с расширеним `.log` имена которых начинается на `crash.`
- все файлы с именами `crash.log`, `override.tf`, `override.tf.json`, `.terraformrc`, `terraform.rc`
- все файлы, имя которых оканчивается на `_override.tf` и `_override.tf.json`
