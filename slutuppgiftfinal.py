import datetime
import pandas as pd


class Book():

    def __init__(self, title, author, borrow_date = None, borrowed = False, return_date = None):
        self.title = title
        self.author = author
        self.borrowed = borrowed
        self.borrow_date = borrow_date
        self.return_date = return_date
        
    def return_as_a_dict(self):
        '''
        Returnerar ett bok object som en dict
        '''
        return {
            "author": self.author,
            "title": self.title,
            "borrowed": self.borrowed,
            "borrow_date": self.borrow_date,
            "return_date": self.return_date
        }

class LibrarySystem():

    def __init__(self, name = None):
        self.name = name
        self.books = []


    def add_book(self, title, author):
        '''
        Lägger till en ny book i bibloteket

        Parametrar: 
        - title = titeln av boken som ska läggas till
        - author = författaren för boken som ska läggas till
        '''
        #skapar ett nytt book object med det givna titeln och författaren
        new_book = Book(title = title, author= author)
        #appendar den nyligen skapta boken till listan av böcker i bibloteket
        self.books.append(new_book)
        #kallar på en helper metod att printa bekräftelse meddelandet
        self.print_added_book(new_book)

    def remove_book(self, title):
        '''
        Tar bort en bok from bibloteket.

        Parametrar: 
        - title = titeln av boken som ska tas bort
        '''
        #kallar på en helper metod för att hitta boken i bibloteket med hjälp av dens titel
        book_to_remove = self.find_book_by_title(title)
        #kollar för att se om boken blev hittat i bibloteket
        if book_to_remove:
           #tar bort den funna boken från listan av böcker i bibloteket
           self.books.remove(book_to_remove)
           #kallar på en helper metod för att printa ut bekräftelse meddelandet
           self.print_removed_book(book_to_remove)
        else:
            #kallar på en helper metod för att printa när boken inte blir hittad
            self.print_book_not_found(title)
           
    def borrow_book(self, title):
        '''
        Lånar en bok från bibloteket

        Parametrar: 
        - title = titeln av boken som bli utlånad
        '''
        #kallar på en helper metod för att hitta boken i bibloteket med hjälp av dens titel
        book_to_borrow = self.find_book_by_title(title)
        #kollar för att se om boken blev hittat i bibloteket
        if book_to_borrow:
            #kallar på en helper metod för att uppdatera lånestatusen på boken
            self.update_borrow_status(book_to_borrow)
        else:
            #kallar på en helper metod för att printa ett meddelande om boken inte blir hittad
            self.print_book_not_found(title)

    def return_book(self, title, return_date):
        '''
        Returnerar en utlånad bok till bibloteket
        
        Parametrar:
        - title = titeln av boken som ska lämnas tillbaka
        - return_date = datumet när boken blir returnerad
        '''
        #kallar på en helper metod för att hitta boken med hjälp av dens titel
        book_to_return = self.find_book_by_title(title)
        #kollar om boken blev hittad i bibloteket
        if book_to_return:
            #kallar på en helper metod för att uppdatera lånestatusen av boken
            self.update_return_status(book_to_return, return_date)
        else:
            #kallar på en helper metod för att printa ut ett meddelande när boken inte blir hittad
            self.print_book_not_found(title)
    
    
    def is_book_available(self, title):
        '''
        Kollar om en bok är tillgänglig att bli utlånad
        
        Parametrar:
        - title = titeln av boken som ska bli kollad om den är tillgänglig
        '''
        #kallar på en helper metod för att hitta boken i bibloteket med hjälp av dens titel
        book = self.find_book_by_title(title)
        #kollar om boken blev hittad i bibloteket
        if book:
            #kallar på en helper metod för att printa tillgänglighets statusen på boken
            self.print_availability_status(book)
            return True
        else:
            #kallar på en helper metod för att printa ut ett meddelande när boken inte blir hittad
            self.print_book_not_found(title)
            return False

    
    def display_available_books(self):
        '''
        Visar alla böcker som är tillgängliga att bli utlånade i bibloteket
        '''
        #kallar på en helper metod för att få en lista av tillgängliga böcker som dicter
        available_books = self.get_available_books()
        #kollar om det finns några tillgängliga böcker i bibloteket
        if available_books:
            #kallar på en helper metod för att skriva ut info om dom böcker tillgängliga för att bli utlånade
            self.print_all_available_books(available_books)
            return True       
        else:
            #kallar på en helper metod för att skriva ut ett meddelande om det inte är några böcker som kan bli utlånade i bibloteket
            self.print_no_available_books()
            return False
       
    def calculate_days_borrowed(self, borrow_date, return_date): 
        '''
        Räknar ut hur många dagar en bok har blivit utlånad
        
        Parametrar:
        - borrow_date = datumet när boken blev utlånad
        - return_date = datumet när boken blev returnerad
        '''
        #räknar ut skillnaden i dagar mellan retur datumet och lånedatumet sen returnerar svaret i en variabel
        days_borrowed = (return_date - borrow_date).days
        return days_borrowed
    
    def find_book_by_title(self,title):
        ''' 
        Hittar en bok i bibloteket med hjälp av dens titel
        
        Parametrar:
        - title = titeln av boken som ska bli hittad

        Returnera:
        - Book objectet om det blir hittat annars None
        '''
        #itererar genom en lista av böcker i bibloteket
        for book in self.books:
            #kollar om titeln av den nuvarande boken i iterationen matchar den givna bok titeln
            if book.title == title:
                #returnerar bok objectet om en matchning hittas
                return book
        #returnerar None om ingen bok blir hittadd
        return None
    
    def update_borrow_status(self,book):
        '''
        Uppdaterar lånestatusen på en bok
        
        Parametrar:
        - book = namnet på det book object vars lånestatus behöver bli uppdaterad
        '''
        #kollar så att boken inte redan är utlånad
        if not book.borrowed:
            #uppdaterar lånestatusen och utlåningsdatumet av boken
            book.borrowed = True
            book.borrow_date = datetime.datetime.today()
            #kallar på en helper metod för att skriva ut ett bekräftelse meddelande
            self.print_borrowed_status(book.title)
        else:
            #kallar på en helper metod för att skriva ut ett meddelande om boken redan blivit utlånad
            self.print_already_borrowed(book.title)

    def update_return_status(self,book, return_date):
        '''
        Uppdaterar return statusen av en utlånad bok
        
        Parametrar:
        - book = book objectet vars return status behöver bli uppdaterad
        - return_date = datumet när boken blev returnerad
        '''
        #kollar om bokar utlånad i nuläget
        if book.borrowed:
           #uppdaterar retur statusen, retur datumet och räknar ut hur många dagar boken blivit utlånad
           book.borrowed = False
           book.return_date = return_date
           days_borrowed = self.calculate_days_borrowed(borrow_date=book.borrow_date, return_date=return_date)
           #kallar på en helper metod för att printa ut retur informationen
           self.print_return_status(book, days_borrowed) 
        else:
            #kallar på en helper metod för att printa ut ett meddelande om boken inte är utlånad
            self.print_not_borrowed(book.title)

    def get_available_books(self):
        '''
        Skapar en lista av dicts för alla tillgängliga böcker i bibloteket
        
        Returnerar:
        - En lista av dicts som representerar alla tillgängliga böcker
        '''
        #initierar en tom lista för att förvara alla dicts av tillgängliga böcker
        available_books = []
        #itererar genom listan av böcker i bibloteket
        for book in self.books:
            #kollar så att boken inte redan är utlånad
            if not book.borrowed:
                #appendar dict representation av boken till listan
                available_books.append(book.return_as_a_dict())
        #returnerar listan av tillgängliga böcker, nu som en lista av dicts och inte en lista av object
        return available_books

    def print_added_book(self, book):
        print(f"The book {book.title} by {book.author} is added to the {self.name}")

    def print_removed_book(self, book):
        print(f"\nThe book {book.title} is removed from the {self.name}")

    def print_book_not_found(self, title):
        print(f"\nThe book {title} does not exist in the {self.name}")

    def print_borrowed_status(self, title):
        print(f"- {title} is now borrowed")

    def print_already_borrowed(self, title):
        print(f"The book {title} has already been borrowed")

    def print_return_status(self, book, days_borrowed):
        #kollar om boken blivit utlånad i mer än 14 dagar
        if days_borrowed > 14:
            #printar ut information om hur länge boken blivit utlånad och hur många dagar för mycket den blivit utlånad
            print(f"The book {book.title} has been borrowed for {days_borrowed} days and is {(days_borrowed - 14)} day/days overdue")
        else:
            #printar ut information om boken blivit återlämnad i tid
            print(f"The book {book.title} has been borrowed for {days_borrowed} days and has been returned on time")
        print(f"- {book.title} has now been returned,thank you for using {self.name} for loaning books\n")

    def print_not_borrowed(self, title):
        print(f"The book {title} is not currently borrowed")

    def print_availability_status(self, book):
        print(f"The book {book.title} is available at {self.name}")

    def print_no_available_books(self):
        print(f"There are no books available for loan in {self.name}")

    def print_all_available_books(self, books):
        '''
        Printar ut information om all tillgängliga böcker i bibloteket
        
        Parametrar:
        - books = en lista av dicts som representerar alla tillgängliga böcker
        '''
        #skapar en Dataframe från listan av dicts
        df = pd.DataFrame(books)
        #printar ut en Rubrik för dom tillgängliga böckerna
        print("\nAvailable Books")
        #itererar igenom dataframen och printar ut author och titeln av varje bok som är tillgänglig
        for index in df.index:
            print(f"{df['author'][index]} - {df['title'][index]}")
        print("\n")

if __name__ == "__main__":
    #skapar en instans av classen LibrarySystem samt sätter dens namn till IHM University Library
    library = LibrarySystem(name = "IHM University Library")

    #lägger till två böcker i bibloteket
    library.add_book(author = "Robert Jordan", title = "Wheel of time")
    library.add_book(author = "Brandon Sanderson", title = "Mistborn")
    library.add_book(author = "Frank Herbert", title = "Dune")

    #tar bort en bok från bibloteket
    library.remove_book(title= "Wheel of time")
    library.remove_book(title = "Journey to the center of the earth")

    #lägger till boken igen för att kunna se att metoden kan fungera åt båda hållen när jag kollar tillgänglighet
    library.add_book(author = "Robert Jordan", title = "Wheel of time")

    #lånar en bok från bibloteket
    library.borrow_book(title = "Mistborn")
    library.borrow_book(title = "Wheel of time")
    library.borrow_book(title = "Journey to the center of the earth")

    #lämnar tillbaka en bok till bibloteket
    library.return_book(title = "Mistborn", return_date = datetime.datetime.today() + datetime.timedelta(days=15 ))
    library.return_book(title = "Journey to the center of the earth", return_date = datetime.datetime.today() + datetime.timedelta(days=15))

    #kollar om en bok finns tillgänglig på bibloteket
    library.is_book_available(title = "Mistborn")
    library.is_book_available(title = "Wheel of time")

    #skriver ut dom nuvarande tillgängliga böckerna i bibloteket
    library.display_available_books()

    
