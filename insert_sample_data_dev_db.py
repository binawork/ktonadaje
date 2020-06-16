from app import db
from app import Event, Category


def main():
    db.create_all()

    ho = Category(title="hobby")
    ps = Category(title="psychologia")
    co = Category(title="programowanie")
    rr = Category(title="związki")
    lm = Category(title="muzyka")
    st = Category(title="live stream")

    ev1 = Event(
        title="Zarządzanie sobą w kryzysie tożsamości",
        host_name="prof. Henryk Sienkiewicz",
        url="https://www.youtube.com/watch?v=J53UK_bul5Y",
        categories=[ps]
    )

    ev2 = Event(
        title="Python w terrarium, czyli o wirtualnych środowiskach",
        host_name="Jakub Wężowy",
        url="https://www.youtube.com/watch?v=J53UK_bul5Y",
        categories=[co]
    )

    ev3 = Event(
        title="Z szydełkowaniem na przeciw COVID-19",
        host_name="Grażka Szydełkowa",
        url="https://www.youtube.com/watch?v=J53UK_bul5Y",
        categories=[ho]
    )

    ev4 = Event(
        title="Programowanie ludzkiego mózgu z wykorzystaniem pakietu numpy \
        i anaconda",
        host_name="Jakub Wężowy",
        url="https://www.youtube.com/watch?v=J53UK_bul5Y",
        categories=[ho, co]
    )

    ev5 = Event(
        title="Szukanie w stogu siana, czyli miłość w czasie zarazy",
        host_name="Agnieszka Buchałka",
        url="https://www.youtube.com/watch?v=J53UK_bul5Y",
        categories=[rr]
    )

    ev6 = Event(
        title="PsyTrans TECHNO Party ELO320",
        host_name="DJ Kolbas",
        url="https://www.youtube.com/watch?v=J53UK_bul5Y",
        categories=[lm, st]
    )

    categories = [
        "joga",
        "fitness",
        "czytanie książek na głos",
        "terapia grupowa",
        "zajęcia teatralne",
        "gotowanie",
    ]
    obj_categories = [Category(title=cat) for cat in categories]

    db.session.add_all([ho, ps, co, ev1, ev2, ev3, ev4, ev5, ev6])
    db.session.add_all(obj_categories)

    db.session.commit()
    db.session.close()


if __name__ == '__main__':
    main()
