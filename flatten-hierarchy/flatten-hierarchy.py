import glob, shutil
target_dir = 'pranav/output'
path_list = glob.glob('pranav/input/**/README.md', recursive=True)
for path in path_list:
    parent_of_readme = path.split('/')[-2]
    shutil.copy(path, f'{target_dir}/{parent_of_readme}.md')
