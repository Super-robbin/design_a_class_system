"""
1. Describe the Problem
Typically you will be given a short statement that does this called a user story.
In industry, you may also need to ask further questions to clarify aspects of the problem.

2. Design the Class System
Diagram in Design_class_system.excalidraw
"""

class DiaryEntry:
    # User-facing properties:
    #   title: string
    #   contents: string

    def __init__(self, title, contents):
        # Parameters:
        #   title: string
        #   artist: string
        # Side-effects:
        #   Sets the title and artist properties
        pass # No code here yet

    def count_words(self):
        # Returns:
        #    An integer representing the number of words in the contents
        pass # No code here yet

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        pass # No code here yet
        
    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        pass
        
class Todo:
    # Public Properties:
    #   task: a string representing the task to be done

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        pass

class PhoneNumbers:
    # User-facing properties:
    #   name: string
    #   contact: string
    #   contact_number: a boolean representing whether the contact is a phone number

    def __init__(self, name, contact):
        # Parameters:
        #   name: a string
        #   contact: a string
        # Side-effects:
        #   Sets the name and contact properties
        #   Sets the complete property to False
        pass

    def is_phone_contact(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass
        
class Diary:
    def __init__(self):
        pass

    def add_entries(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        pass

    def add_todo(self, task):
        # Parameters:
        #   task: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the task to the todo list
        pass

    def add_contacts_to_entries(self, contact):
        # Parameters:
        #   contact: an instance of PhoneNumbers
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the contact to the entries list
        pass

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry and PhoneNumbers
        pass

    def count_words(self):
        # Returns:
        #    An integer representing the sum of all the entries #word_count
        pass # No code here yet

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        pass

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass

    def phone_numbers_list(self):
        # Returns:
        #   An instance of PhoneNumbers representing only contacts where contaxt
        #   is a phone number.
        pass

"""
3. Create Examples as Integration Tests
# EXAMPLE

Initially there are no entries
"""
def test_initially_has_no_entries():
    all_diary = Diary()
    assert all_diary.all() == []

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
def test_add_multiple_entries():
    all_diary = Diary()
    task1 = Todo('Cook the dinner')
    task2 = Todo('Clean the flat')
    all_diary.add_entries(task1)
    all_diary.add_entries(task2)
    assert all_diary.all() == [task1, task2]

"""
Given I have two contacts
I can add them to the entries just if the contact == phone number
"""
def test_only_add_contacts_with_phone_numbers():
    all_diary = Diary()
    contact1 = PhoneNumbers('Bob', 'abcderr@gmail.com')
    contact2 = PhoneNumbers('Alina', '08976225876')
    all_diary.add_entries(contact1)
    all_diary.add_entries(contact2)
    contact2.is_phone_contact()
    assert all_diary.phone_numbers_list() == [contact2]
"""

Given I add two entries
And I call #count_words
I can get the sum of all words in the content of the diary entries
"""
def test_count_words_returns_count_of_all_words_in_all_entry_contents():
    all_diary = Diary()
    entry1 = DiaryEntry('31 July', 'Do some coding')
    entry2 = DiaryEntry('01 August', 'Go to the cinema')
    all_diary.add(entry1)
    all_diary.add(entry2)
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
    all_diary.add(entry1)
    all_diary.add(entry2)
    assert all_diary.reading_time(2) == 3

"""
Given I add two entries, one long and one short
And I call #find_the_best_entry_for_reading_time
With a wpm and minuts that means I can only read the short one
Then #find_the_best_entry_for_reading_time returns the shorter one
"""
def find_the_best_entry_for_reading_time_returns_entry_that_fits_in_time():
    all_diary = Diary()
    entry1 = DiaryEntry('31 July', 'One two three')
    entry2 = DiaryEntry('01 August', 'One two three four five six seven')
    all_diary.add(entry1)
    all_diary.add(entry2)
    assert all_diary.find_best_entry_for_reading_time(2, 3) == entry1

"""
Encode one of these as a test and move to step 4.

4. Create Examples as Unit Tests
# EXAMPLE

file test_unit_diary.py

Initially there are no entries
"""
def test_initially_has_no_entries():
    all_diary = Diary()
    assert all_diary.all() == []

"""
Initially, word count is zero
"""
def test_initially_has_no_entries():
    all_diary = Diary()
    assert all_diary.count_words() == 0

"""
file test_unit_diary_entry.py

When i initialise with a title and contents
I can get that titles and contents back
"""
def test_constructs_and_gets_title_and_contents():
    diary_entry = DiaryEntry('My Title', 'My Contents')
    assert diary_entry.title == 'My Title'
    assert diary_entry.contents == 'My Contents'

"""
When i initialise with six-word contents
Then #count_words should return six
"""
def test_count_words():
    my_entry = DiaryEntry('29 July', 'Today we went out for lunch')
    assert my_entry.count_words() == 6

"""
When i initialise with five-word contents
Then #reading_time with a wpm of 2 should return 3
"""
def test_reading_time():
    diary_entry = DiaryEntry("My Title", 'One two three four five')
    assert diary_entry.reading_time(2) == 3

"""
When i initialise with five-word contents
Then at first, #reading_chunk should return the first chunk
readable in the time
"""
def test_readable_chunk_first_chunk():
    diary_entry = DiaryEntry("My Title", 'One two three four five')
    assert diary_entry.reading_chunk(2, 1) == 'One two'

"""
file test_unit_todo.py

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
def test_constructs_and_gets_task_and_contents():
    tasks = Todo('Cook the dinner')
    tasks.mark_complete()
    assert tasks.complete == True

"""
file test_unit_phone_numbers.py

When i initialise with a name and contact
I can get those names and contacts back
"""
def test_constructs_and_gets_name_and_contact():
    contacts_details = PhoneNumbers('Rob', '0987656678')
    assert contacts_details.name == 'Rob'
    assert contacts_details.contact == '0987656678'

"""
When marking a contact as #is_phone_contact, if a contact == False
We switch contact = True
"""
def test_mark_contact_as_phone_number():
    contact_details = PhoneNumbers('Rob', '0987656678')
    contact_details.is_phone_contact()
    assert contact_details.contact == True

"""
Encode one of these as a test and move to step 5.

5. Implement the Behaviour
For each example you create as a test, implement the behaviour that allows the class to behave according to your example.

Then return to step 3 until you have addressed the problem you were given. You may also need to revise your design, for example if you realise you made a mistake earlier.
"""