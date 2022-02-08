from ostoskori import Ostoskori
from tuote import Tuote

def main():
    kori = Ostoskori()

    maito = Tuote("Maito", 3)

    kori.lisaa_tuote(maito)
    kori.lisaa_tuote(maito)

    for i in kori.ostoslista:
        print('haloo')
        print(i.lukumaara())


if __name__ == "__main__":
    main()