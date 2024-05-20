from lib.BirthdayTracker import *

"""
Given no name and birthdate
output an empty list
"""
def test_initial_output_is_empty_list():
    input = BirthdayTracker()
    result = input.view_all()
    assert result == []

"""
Given a name and birthdate
list out name and birthdate
"""
def test_one_name_and_birthdate():
    input = BirthdayTracker()
    input.add("John", "1983-01-22")
    result = input.view_all()
    assert result == [{"John": "1983-01-22"}]

"""
Give a name and new birthdate
update persons birthdate
"""

def test_one_name_and_birthdate():
    input = BirthdayTracker()
    input.add("John", "1983-01-22")
    input.update_birthdate("John", "1984-01-22")
    result = input.view_all()
    assert result == [{"John": "1984-01-22"}]