from aiogram import types

from database.models import engine, Base, Session, User

Base.metadata.create_all(engine)


def add_user(message: types.Message) -> User:
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    with Session() as session:
        result = get_user_by_id(int(user_id))
        if result is None:
            new_user = User(user_id=user_id, username=username, first_name=first_name, last_name=last_name)
            session.add(new_user)
            session.commit()
        return result


def get_user_by_id(user_id) -> User:
    with Session() as session:
        result = session.query(User).filter_by(user_id=int(user_id)).first()
        return result


def check_user(user_id: int) -> bool:
    with Session() as session:
        result = bool(session.query(User).filter_by(user_id=user_id).first())
    return result
