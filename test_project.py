from project import add_task, remove_task, view_tasks, tasks

def test_add_task():
    tasks.clear()
    add_task("Test Task")
    assert tasks == ["Test Task"]

def test_remove_task():
    tasks.clear()
    add_task("Task 1")
    add_task("Task 2")
    remove_task(0)
    assert tasks == ["Task 2"]

def test_view_tasks(capsys):
    tasks.clear()
    add_task("Task 1")
    add_task("Task 2")
    view_tasks()
    captured = capsys.readouterr()
    assert "0. Task 1" in captured.out
    assert "1. Task 2" in captured.out
