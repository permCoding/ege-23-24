import requests
import json


# url = "https://kompege.ru/api/v1/task/11950"
url = "https://kompege.ru/api/v1/task/number/18"
arr = requests.get(url).json()

task = arr[0]
# print(json.dumps(task, ensure_ascii=False, indent=2))

host = 'https://kompege.ru'
obj = {
    'theme_num': task['number'],
    'task_id': task['taskId'],
    'text': task['text'],
    'answers': task['key'].split(),
    'files': {
        'link': host + task['files'][0]['url'],
        'name': task['files'][0]['name']
    }
}

print(json.dumps(obj, ensure_ascii=False, indent=4))

# https://kompege.ru/task
# https://kompege.ru/api/v1/task/number/18

