import os

for i in range(1, 365 + 1):
    d = str(i) + " day ago"
    with open("load.txt", "a") as file:
        file.write(d)
    os.system("git add load.txt")
    os.system('git commit --date="' + d + '" -m "first commit"')
os.system("git push -u origin master")
