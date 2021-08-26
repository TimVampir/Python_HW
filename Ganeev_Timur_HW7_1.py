import os.path

project_dir = 'my_project'
my_dir = ['settings', 'mainapp', 'adminapp', 'authapp']

for i in my_dir:
    os.makedirs(os.path.join(os.curdir, project_dir, i), exist_ok=True)