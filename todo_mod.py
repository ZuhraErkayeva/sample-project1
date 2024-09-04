from classwork import main_func,add_task,remove_task,sort_by_due_date,view_tasks,search_task,mark_task_as_completed,display_overdue_tasks,close_application
todos = {}
print("Todo ilovaga xush kelibsiz")
while True:
    main_func()
    choose = int(input('Tanlovingizni kiriting: '))
    if choose == 1:
        add_task(todos)
    elif choose == 2:
        remove_task(todos)
    elif choose == 3:
        view_tasks(todos)
    elif choose == 4:
        sort_by_due_date(todos)
    elif choose == 5:
        search_task(todos)
    elif choose == 6:
        display_overdue_tasks(todos)
    elif choose == 7:
        mark_task_as_completed(todos)
    elif choose == 8:
        close_application(todos)
        break