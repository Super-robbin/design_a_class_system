"""
1. Describe the Problem
Typically you will be given a short statement that does this called a user story.
In industry, you may also need to ask further questions to clarify aspects of the problem.

2. Design the Class System
Design the interfaces of each of your classes and how they will work together to achieve the job of the program.
You can use diagrams to visualise the relationships between classes.


class MusicLibrary:
    # User-facing properties:
    #   tracks: list of instances of Track

    def __init__(self):
        pass # No code here yet

    def add(self, track):
        # Parameters:
        #   track: an instance of Track
        # Side-effects:
        #   Adds the track to the tracks property of the self object
        pass # No code here yet

    def search_by_title(self, keyword):
        # Parameters:
        #   keyword: string
        # Returns:
        #   A list of the Track objects that have titles that include the keyword
        pass # No code here yet


class Track:
    # User-facing properties:
    #   title: string
    #   artist: string

    def __init__(self, title, artist):
        # Parameters:
        #   title: string
        #   artist: string
        # Side-effects:
        #   Sets the title and artist properties
        pass # No code here yet

    def format(self):
        # Returns:
        #   A string of the form "TITLE by ARTIST"
        pass # No code here yet

"""
3. Create Examples as Integration Tests
Create examples of the classes being used together in different situations
and combinations that reflect the ways in which the system will be used.
# EXAMPLE


Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""

library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]

"""
Encode one of these as a test and move to step 4.

4. Create Examples as Unit Tests
Create examples, where appropriate, 
of the behaviour of each relevant class at a more granular level of detail.
# EXAMPLE

Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"

"""
Encode one of these as a test and move to step 5.

5. Implement the Behaviour
For each example you create as a test, implement the behaviour that allows the class to behave according to your example.

Then return to step 3 until you have addressed the problem you were given. You may also need to revise your design, for example if you realise you made a mistake earlier.
"""