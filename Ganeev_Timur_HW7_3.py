import os

project_dir = 'my_project'
my_dir = 'templates'

dirs = os.walk(project_dir)
for x, y, _ in dirs:
    for i in y:
        new_path = os.path.join(os.curdir, project_dir, os.sep.join(x.split(os.sep)[1:]), i)
        print(x.split(os.sep))
        os.makedirs(new_path, exist_ok=True)
