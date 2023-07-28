task=input('Enter your name')
task_count=len(set(task))
if task_count>10:
    print(True)
else:
    print(False)