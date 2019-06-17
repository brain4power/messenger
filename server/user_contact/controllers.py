from database.models import Session, UserContact, User
from protocol import make_response


def add_contact(request):
    owner_login = request.get('user')
    contact_login = request.get('contact')
    session = Session()
    owner_id = User.get_user_id_by_login(session, owner_login)
    contact_id = User.get_user_id_by_login(session, contact_login)
    if contact_id:
        UserContact.add_contact(session, owner_id, contact_id)
        session.commit()
        return make_response(request, 200)


def del_contact(request):
    owner_login = request.get('user')
    contact_login = request.get('contact')
    session = Session()
    owner_id = User.get_user_id_by_login(session, owner_login)
    contact_id = User.get_user_id_by_login(session, contact_login)
    if contact_id:
        UserContact.del_contact(session, owner_id, contact_id)
        session.commit()
        return make_response(request, 200)


def get_contacts(request):
    user = request.get('user')
    session = Session()
    user_id = User.get_user_id_by_login(session, user)
    data = str(UserContact.get_user_contacts(session, user_id))
    session.commit()
    return make_response(request, 200, data)


def get_all_users(request):
    session = Session()
    data = str(User.get_all_users(session))
    session.commit()
    return make_response(request, 200, data)
