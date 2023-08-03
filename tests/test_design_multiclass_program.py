from lib.design_multiclass_program_behaviour import DiaryEntry
from lib.design_multiclass_program_behaviour import Diary
from lib.design_multiclass_program_behaviour import Todo
from lib.design_multiclass_program_behaviour import PhoneNumbers

"""
Given I add two entries
I can see them represented in a list, with the right format
"""
def test_add_multiple_entries():
    all_diary = Diary()
    entry1 = DiaryEntry('31 July', 'Do some coding')
    entry2 = DiaryEntry('01 August', 'Go to the cinema')
    all_diary.add_entries(entry1)
    all_diary.add_entries(entry2)
    assert all_diary.all() == [entry1, entry2]

"""
Given I add two tasks
I can keep them in a todo list
"""
def test_add_multiple_todos():
    todos = Diary()
    task1 = Todo('Cook the dinner')
    task2 = Todo('Clean the flat')
    todos.add_todo(task1)
    todos.add_todo(task2)
    assert todos.todos_list == [task1, task2]

"""
Given I have two contacts
I can add them to the entries just if the contact == phone number
"""
def test_only_add_contacts_with_phone_numbers():
    contact_details = Diary()
    contact1 = PhoneNumbers('Bob', 'abcderr@gmail.com')
    contact2 = PhoneNumbers('Alina', '08976225876')
    contact_details.add_contacts_to_entries(contact1)
    contact_details.add_contacts_to_entries(contact2)
    assert contact_details.phone_numbers_list() == ['08976225876']

"""
Given I add two entries
And I call #count_words
I can get the sum of all words in the content of the diary entries
"""
def test_count_words_returns_count_of_all_words_in_all_entry_contents():
    all_diary = Diary()
    entry1 = DiaryEntry('31 July', 'Do some coding')
    entry2 = DiaryEntry('01 August', 'Go to the cinema')
    all_diary.add_entries(entry1)
    all_diary.add_entries(entry2)
    assert all_diary.count_words() == 7


"""
Given I add two entries with a total length of 5
And I call #reading_time with a wpm of 2
Then the total reading time should be 3
"""
def test_reading_time_returns_time_to_read_all_entries():
    all_diary = Diary()
    entry1 = DiaryEntry('31 July', 'Do something')
    entry2 = DiaryEntry('01 August', 'Go get food')
    all_diary.add_entries(entry1)
    all_diary.add_entries(entry2)
    assert all_diary.reading_time(2) == 3

"""
Given I add two entries, one long and one short
And I call #find_the_best_entry_for_reading_time
With a wpm and minuts that means I can only read the short one
Then #find_the_best_entry_for_reading_time returns the shorter one
"""
def test_find_the_best_entry_for_reading_time_returns_entry_that_fits_in_time():
    all_diary = Diary()
    entry1 = DiaryEntry('31 July', 'One two three')
    entry2 = DiaryEntry('01 August', 'One two three four five six seven')
    all_diary.add_entries(entry1)
    all_diary.add_entries(entry2)
    assert all_diary.find_best_entry_for_reading_time(2, 3) == entry1
