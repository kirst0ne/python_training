

def test_delete_first_contact(app):
    app.session.home_page()
    app.contact.delete_first_contact()
