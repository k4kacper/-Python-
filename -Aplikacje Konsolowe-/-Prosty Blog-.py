"""Prosty Blog:
Stwórz aplikację konsolową do zarządzania blogiem z klasami Post, Komentarz. Aplikacja powinna umożliwiać dodawanie postów, dodawanie komentarzy do postów oraz wyświetlanie listy postów i komentarzy."""

class Post:
    def __init__(self, tytul, tresc):
        self.tytul = tytul
        self.tresc = tresc
        self.komentarze = []

    def dodaj_komentarz(self, komentarz):
        self.komentarze.append(komentarz)

    def usun_komentarz(self, indeks):
        if 0 <= indeks < len(self.komentarze):
            del self.komentarze[indeks]

    def wyswietl_post(self):
        print(f"\nTytuł: {self.tytul}")
        print(f"Tresc: {self.tresc}")
        print("Komentarze:")
        if self.komentarze:
            for i, komentarz in enumerate(self.komentarze, start=1):
                print(f"{i}. {komentarz}")
        else:
            print("Brak komentarzy.")

class Blog:
    def __init__(self):
        self.posty = []

    def dodaj_post(self, tytul, tresc):
        self.posty.append(Post(tytul, tresc))

    def usun_post(self, indeks):
        if 0 <= indeks < len(self.posty):
            del self.posty[indeks]

    def dodaj_komentarz_do_posta(self, indeks, komentarz):
        if 0 <= indeks < len(self.posty):
            self.posty[indeks].dodaj_komentarz(komentarz)

    def wyswietl_posty(self):
        print("\n===== LISTA POSTÓW =====")
        if not self.posty:
            print("Brak postów na blogu.")
        else:
            for i, post in enumerate(self.posty, start=1):
                print(f"{i}. {post.tytul}")
        print("========================\n")

def menu():
    blog = Blog()

    while True:
        print("\nWybierz opcję:")
        print("1. Dodaj post")
        print("2. Usuń post")
        print("3. Dodaj komentarz do posta")
        print("4. Wyświetl posty")
        print("5. Wyświetl szczegóły posta")
        print("6. Wyjdź")

        wybor = input("\nTwój wybór: ")

        if wybor == "1":
            tytul = input("Podaj tytuł posta: ")
            tresc = input("Podaj treść posta: ")
            blog.dodaj_post(tytul, tresc)

        elif wybor == "2":
            blog.wyswietl_posty()
            indeks = int(input("Podaj numer posta do usunięcia: ")) - 1
            blog.usun_post(indeks)

        elif wybor == "3":
            blog.wyswietl_posty()
            indeks = int(input("Podaj numer posta, do którego chcesz dodać komentarz: ")) - 1
            komentarz = input("Wpisz komentarz: ")
            blog.dodaj_komentarz_do_posta(indeks, komentarz)

        elif wybor == "4":
            blog.wyswietl_posty()

        elif wybor == "5":
            blog.wyswietl_posty()
            indeks = int(input("Podaj numer posta do wyświetlenia: ")) - 1
            if 0 <= indeks < len(blog.posty):
                blog.posty[indeks].wyswietl_post()
            else:
                print("Niepoprawny numer posta.")

        elif wybor == "6":
            print("Zakończenie programu.")
            break

        else:
            print("Nieprawidłowa opcja, spróbuj ponownie.")

menu()