from lib.design_multiclass_program_behaviour import Diary

"""
Initially there are no entries
"""
def test_initially_has_no_entries():
    all_diary = Diary()
    assert all_diary.all() == []

"""
Initially, word count is zero
"""
def test_initially_has_no_entries_words():
    all_diary = Diary()
    assert all_diary.count_words() == 0