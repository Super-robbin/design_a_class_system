from lib.design_multiclass_program_behaviour import PhoneNumbers

"""
When i initialise with a name and contact
I can get those names and contacts back
"""
def test_constructs_and_gets_name_and_contact():
    contacts_details = PhoneNumbers('Rob', '0987656678')
    assert contacts_details.name == 'Rob'
    assert contacts_details.contact == '0987656678'
