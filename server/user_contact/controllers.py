from database.models import Session, UserContact, User
from protocol import make_response


def add_contact(request):
    pass


def del_contact(request):
    pass


def get_contacts(request):
    user = request.get('user')
    session = Session()
    user_id = User.get_user_id_by_login(session, user)
    data = UserContact.get_user_contacts(session, user_id)
    session.commit()
    return make_response(request, 202, data)
