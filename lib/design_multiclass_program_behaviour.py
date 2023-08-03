from math import ceil

class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents

    def count_words(self):
        return len(self.contents.split())

    def reading_time(self, wpm):
        return ceil(self.count_words() / wpm)
        
    def reading_chunk(self, wpm, minutes):
        readable_chunk_length = wpm * minutes
        words = self.contents.split()
        return " ".join(words[:readable_chunk_length])
        
class Todo:
    def __init__(self, task):
        self.task = task
        self.complete = False

    # def mark_complete(self):
    #     if self.task == False:
    #         self.task = True

class PhoneNumbers:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        
class Diary:
    def __init__(self):
        self.entries = []
        self.todos_list = []

    def add_entries(self, entry):
        self.entries.append(entry)

    def add_todo(self, task):
        self.todos_list.append(task)

    def add_contacts_to_entries(self, contact):
        self.entries.append(contact)

    def all(self):
        return self.entries
    
    def count_words(self):
        total = 0
        for entry in self.entries:
            total += entry.count_words()
        return total

    def reading_time(self, wpm):
        word_count = self.count_words()
        return ceil(word_count / wpm)

    def find_best_entry_for_reading_time(self, wpm, minutes):
        words_the_user_could_read = wpm * minutes
        most_readable = None
        longest_found_so_far = 0
        for entry in self.entries:
            if entry.count_words() <= words_the_user_could_read:
                if entry.count_words() > longest_found_so_far:
                    most_readable = entry
                    longest_found_so_far = entry.count_words()
        return most_readable

    def phone_numbers_list(self):
        phone_numbers = []
        for entry in self.entries:
            for word in entry.contact.split():
                if word.isdigit() and len(word) == 11 and word[0] == '0':
                    phone_numbers.append(word)
        return phone_numbers