# import libraries here


def train_or_load_traffic_sign_model(train_positive_images_paths, train_negative_images_path, train_image_labels):
    """
    Procedura prima listu putanja do pozitivnih i negativnih fotografija za obucavanje, liste
    labela za svaku fotografiju iz pozitivne liste

    Procedura treba da istrenira model(e) i da ih sacuva u folder "serialization_folder" pod proizvoljnim nazivom

    Kada se procedura pozove, ona treba da trenira model(e) ako on nisu istranirani, ili da ih samo ucita ako su prethodno
    istrenirani i ako se nalaze u folderu za serijalizaciju

    :param train_positive_images_paths: putanje do pozitivnih fotografija za obucavanje
    :param train_negative_images_path: putanje do negativnih fotografija za obucavanje
    :param train_image_labels: labele za pozitivne fotografije iz liste putanja za obucavanje - tip znaka
    :return: lista modela
    """
    # TODO - Istrenirati modele ako vec nisu istrenirani, ili ih samo ucitati iz foldera za serijalizaciju

    models = []
    return models


def detect_traffic_signs_from_image(trained_models, image_path):
    """
    Procedura prima listu istreniranih modela za detekciju i klasifikaciju saobracajnih znakova i putanju do fotografije na kojoj
    se nalazi novi znakovi koje treda detektovati i klasifikovati

    Ova procedura se poziva automatski iz main procedure pa nema potrebe dodavati njen poziv u main.py

    :param trained_models: Istreniranih modela za detekciju i klasifikaciju saobracajnih znakova
    :param image_path: Putanja do fotografije sa koje treba detektovati 
    :return: Naziv prediktovanog tipa znaka, koordinate detektovanog znaka
    """
    print(image_path)
    # TODO - Detektovati saobracajne znakove i vratiti listu detektovanih znakova:
    # za 2 znaka primer povratne vrednosti[[10, 15, 20, 20, "ZABRANA"], [30, 40, 60, 70, "DRUGI"]]
    detections = [[0, 0, 0, 0, "DRUGI"]]  # x_min, y_min, x_max, y_max, tip znaka
    return detections
