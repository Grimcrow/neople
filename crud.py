from models import User


def create_user(db, user):
    print(user)
    db_user = User(
        name=user.name,
        date_of_birth=user.date_of_birth,
        place_of_birth=user.place_of_birth
    )
    print(db_user)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user