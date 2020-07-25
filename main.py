import os

## Number of days you want to make commits
for i in range(1,365 + 1):
    d = str(i) + ' day ago'
    ## Open a text file and modify it
    with open('load.txt', 'a') as file:
        file.write(d)
    ## Add load.txt to staging area
    os.system('git add load.txt')
    ## Commit it
    os.system('git commit --date="' + d + '" -m "first commit"')

## push the commit to github
os.system('git push -u origin master')  