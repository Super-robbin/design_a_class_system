from lib.design_multiclass_program_behaviour import DiaryEntry

"""
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