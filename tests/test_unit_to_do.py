from lib.design_multiclass_program_behaviour import Todo

"""
When i initialise with a task
I can get that task back
"""
def test_constructs_and_gets_task_and_contents():
    tasks = Todo('Cook the dinner')
    assert tasks.task == 'Cook the dinner'

"""
When marking a task, if a task complete == False
We switch complete = True
"""
# def test_constructs_and_gets_task_and_contents():
#     tasks = Todo('Cook the dinner')
#     tasks.mark_complete()
#     assert tasks.complete == True
