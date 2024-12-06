def delete_task(task_list, task):
    if task in task_list:
        task_list.remove(task)
    return task_list
